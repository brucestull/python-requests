import requests
import os
from dotenv import load_dotenv


load_dotenv()

url = f"{os.getenv('SERVER_ROOT_URL')}{os.getenv('API_ROOT')}{os.getenv('FIRST_ENDPOINT')}"


response = requests.get(url)
print("response.url: ", response.url)
# `response.text` contains a string returned by the API, we need to use `response.json()` to get a json object:
print("response.text: ", response.text)
