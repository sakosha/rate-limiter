from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(0.001, 0.01)

    @task
    def hello_world(self):
        self.client.get("/api/")
