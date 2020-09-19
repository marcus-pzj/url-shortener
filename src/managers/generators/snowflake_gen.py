import random
from utils.snowflake import SnowflakeClient
from utils import base62

from managers.generators import UniqueShortKeyGenerator

class SnowflakeGenerator(UniqueShortKeyGenerator):
    DATA_CENTER_ID = 0
    WORKER_ID = 29

    def __init__(self):
        self.client = SnowflakeClient(self.DATA_CENTER_ID, self.WORKER_ID)

    def generate(self, url) -> str:
        res = base62.encode(self.client.next_id())
        return res
