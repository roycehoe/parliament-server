import redis
from constants import DEFAULT_REDIS_PORT, REDIS_HOST


def get_database() -> redis.Redis:
    return redis.Redis(host=REDIS_HOST, port=DEFAULT_REDIS_PORT, decode_responses=True)
