# TLDR

nginx handles rate-limiting in /nginx/default.conf

run rate-limiter example
```bash
docker compose up
```

see limiting on load.
```bash
pip install locust  # poetry add, uv add, pdm add
locust -H http://localhost:8080
```

# Problem

Your microservice API currently faces performance degradation during traffic spikes due to uncontrolled request bursts from clients

Implement a rate-limiting mechanism within your microservice to ensure API stability and consistent performance. Clearly describe your approach, chosen algorithms, and configurations in README.


# Simple rate limiter on Reverse Proxy/Load balancer level via NGINX.

limit_req_zone $binary_remote_addr zone=one:10m rate=5/s;

Configuration
- we rate limiting per IP, we reserve 10mb for IPs  # okay solution as requests are from clients
- we set limit to 5 RPS per IP
- we allow up to 10 requests right after the limit of 5, so folks could retry if it's a network issue
- we set nginx to limit on /api as it a standard
- nginx is used as it well established & fast. other options could be 
  - traefik (better monitoring, slower under extreme load, doesn't serve static content that could be required)
  - HAProxy (Can handle more load than nginx, not as common in KZ). 

Why on proxy?
- Separation of concerns: we separate our microservice business login (in this case Flask) from rate limiting.
- Scale: now with this setup we can trivially add new instances of our backend, and have simple entrypoint for it via Proxy.
- Goal achieved: now we do not have a performance degradation as we don't receive these requests.

Tradeoffs:
- caller of our api have to handle bad responses, perhaps:
  - retry?
  - put in queue?
  - return error down the line?
  - display error to the user?

![alt text](https://github.com/sakosha/rate-limiter/blob/master/locust.png?raw=true)
