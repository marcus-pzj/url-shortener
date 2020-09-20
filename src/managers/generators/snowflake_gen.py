import requests
import random

from managers.generators import UniqueShortKeyGenerator
from utils import base62
from utils import snowflake

class SnowflakeGenerator(UniqueShortKeyGenerator):

    SNOWFLAKE_ENDPOINT = "http://host.docker.internal:9000/id/test11"

    def __init__(self, snowflake_endpoint=SNOWFLAKE_ENDPOINT):
        self.snowflake_url = snowflake_endpoint

    def generate(self, url) -> str:
        response = requests.get(self.snowflake_url)
        data = int(response.text)

        return base62.encode(data)

class SnowflakeUtilGenerator(UniqueShortKeyGenerator):

    SNOWFLAKE_GENERATOR = snowflake.generator(random.randint(1, 10), random.randint(1, 10))

    def __init__(self, generator=SNOWFLAKE_GENERATOR):
        self._generator = generator

    def generate(self, url) -> str:
        data = next(self._generator) + random.randint(0, 1000)

        return base62.encode(data)