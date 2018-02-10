import redis


class BaseRepository(object):

    def __init__(self, pool):
        self.redis = redis.Redis(connection_pool=pool, decode_responses=True)

    def get_redis(self):
        return self.redis
