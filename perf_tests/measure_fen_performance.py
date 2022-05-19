import time
from locust import HttpUser, task, between, run_single_user


class FenPerfMeasurement(HttpUser):
    wait_time = between(1, 5)

    @task
    def get_fen_base(self):
        self.client.get("/fenBase")
        time.sleep(1)

    @task
    def get_fen(self):
        self.client.get("/fenBase?fen=rnbqkb1r/pppp1ppp/4pn2/8/2PP4/8/PP2PPPP/RNBQKBNR w KQkq - 0 3")
        time.sleep(1)