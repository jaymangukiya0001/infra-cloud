import requests


def main():
    """this function calls a mock server to shorten the url which is passed in the URL of mock server"""
    input_url = input("enter the url:")
    response = requests.get(f"http://localhost:5000/api_call/{input_url}")
    response=response.json()
    print(response["shorten_url"])


if __name__ == "__main__":
    main()
