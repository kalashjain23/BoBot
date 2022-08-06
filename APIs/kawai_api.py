import os

import requests
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("KAWAI_TOKEN")


def get_response(endpoint):
    json = (requests.get(f"https://kawaii.red/api/gif/{endpoint}/token={token}")).json()
    return json['response']

