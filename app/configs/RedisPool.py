import redis

from app.configs.configs import REDIS_HOST, REDIS_PORT, REDIS_DB

POOL = redis.ConnectionPool(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB, decode_responses=True)