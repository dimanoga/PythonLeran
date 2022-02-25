import random
from locust import HttpUser, task

user = ["3-2WU9N735X", "3-2WU9N846F", "3-2WU9NGOHB", "-2WU9N6XJ5", "1234"]
class HelloWorldUser(HttpUser):
    @task
    def hello_world(self):

        random_user = random.randint(0, len(user) - 1)
        self.client.post("/deduplicated_users", json={
            "siebels": [
                user[random_user]
            ]
        })


