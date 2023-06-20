from dataclasses import dataclass
from typing import Optional

import redis
from database import get_database


@dataclass
class CRUDRedis:
    redis: redis.Redis

    def get(self, key: str) -> Optional[str]:
        return self.redis.get(key)

    def create(self, key: str, value: str) -> None:
        self.redis.set(key, value)
        return


crud_redis = CRUDRedis(get_database())
