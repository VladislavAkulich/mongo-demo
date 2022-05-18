import time
from locust import HttpUser, task, between, run_single_user


class DBPerfMeasurement(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_fen_base(self):
        self.client.get("/")
        time.sleep(1)