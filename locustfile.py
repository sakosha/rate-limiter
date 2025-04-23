from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(0.1, 0.2)  # 5-10 запросов в секунду

    @task
    def hello_world(self):
        self.client.get("/")
