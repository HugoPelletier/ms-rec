import random

import redis
from locust import HttpLocust, TaskSet, task

from app.configs.RedisPool import POOL


class PdpBehavior(TaskSet):
    redis = None
    clients = None
    brands = None
    categories = None

    def on_start(self):
        # scan keys to generate random calls to API
        self.redis = redis.Redis(connection_pool=POOL, decode_responses=True)
        self.clients = self.get_clients()
        self.brands = self.get_brands()
        self.categories = self.get_categories()

    def get_clients(self):
        return self.redis.keys('cid:*')

    def get_brands(self):
        return self.redis.keys('product:brand:*')

    def get_categories(self):
        return self.redis.keys('product:category:*')

    @task
    def pdp_category(self):
        self.client.get("/pdp/%s/category/%s" % (random.choice(self.clients), random.choice(self.categories)))

    @task
    def pdp_brand(self):
        self.client.get("/pdp/%s/brand/%s" % (random.choice(self.clients), random.choice(self.brands)))


class WebsiteUser(HttpLocust):
    task_set = PdpBehavior
    min_wait = 0
    max_wait = 0

