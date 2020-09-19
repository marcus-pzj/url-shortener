import requests
import random

from managers.generators import UniqueShortKeyGenerator
from utils import base62

class SnowflakeGenerator(UniqueShortKeyGenerator):

    def __init__(self):
        self.snowflake_url = "http://docker.for.mac.localhost:9000/id/test11"

    def generate(self, url) -> str:
        response = requests.get(self.snowflake_url)
        data = int(response.text)

        return base62.encode(data)
