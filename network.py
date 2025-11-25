import requests
def check_internet():
    try:
        requests.get("https://www.google.com",timeout=5)
        print("internet is working")
    except requests.ConnectionError:
        print("no internet connection")
    if __name__ == "__main__":
        check_internet()

            

