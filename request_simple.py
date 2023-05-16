import requests


url = 'https://api.ipify.org'


response = requests.get(url)
print("response.text: ", response.text)
