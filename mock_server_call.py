import requests


def main():
    """this function calls a mock server to shorten the url which is passed in the URL of mock server"""
    try:
        input_url = input("enter the url:")
        response = requests.get(f"http://localhost:5000/api_call/{input_url}")
        response=response.json()
        if "error" in response:
            print(response["error"])
        else:
            print(response["shorten_url"])
    except requests.exceptions.ConnectionError as e:
        print(e)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
