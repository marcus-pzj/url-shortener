import requests
import random

from managers.generators import UniqueShortKeyGenerator
from utils import base62

class SnowflakeGenerator(UniqueShortKeyGenerator):

    SNOWFLAKE_ENDPOINT = "http://host.docker.internal:9000/id/test11"

    def __init__(self, snowflake_endpoint=SNOWFLAKE_ENDPOINT):
        self.snowflake_url = snowflake_endpoint

    def generate(self, url) -> str:
        response = requests.get(self.snowflake_url)
        data = int(response.text)

        return base62.encode(data)
