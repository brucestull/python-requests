import requests
import pprint


url = 'https://api.ipify.org'


response = requests.get(url)
print("response.url: ", response.url)
print("response.status_code: ", response.status_code)
print("response.encoding: ", response.encoding)
print(response.text)
print("response.headers: ")
pprint.pprint(response.headers)
print("dir(response.headers): ")
pprint.pprint(dir(response.headers))
