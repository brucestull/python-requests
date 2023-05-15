import requests
import pprint


def main():
    response = requests.get('https://api.ipify.org')
    pprint.pprint(response.url)
    pprint.pprint(response.text)
    pprint.pprint(response.status_code)
    pprint.pprint(response.encoding)
    pprint.pprint(response.headers)

if __name__ == "__main__":
    main()
