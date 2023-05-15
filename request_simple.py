import requests


def main():
    response = requests.get('https://api.ipify.org')
    print("response.text: ", response.text)

if __name__ == "__main__":
    main()
