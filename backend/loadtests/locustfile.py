from random import choice, randint

from locust import FastHttpUser, task


class Backend(FastHttpUser):
    @task(0)
    def ping_ok(self):
        self.client.get("ping")

    @task(0)
    def get_exhauster_events(self):
        self.client.get(
            f"events?exhauster_id={randint(0, 5)}&page={randint(1, 10)}&"
            f"size={randint(1, 100)}&sort_order={choice(('ASC', 'DESC'))}"
        )

    @task(1)
    def get_exhausters(self):
        self.client.get("exhausters")

    @task(0)
    def get_exhauster(self):
        self.client.get(f"exhausters/{randint(0, 5)}")
