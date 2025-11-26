import requests
from datetime import datetime


def check_internet():
    sites = ["https://www.google.com",
             "https://www.cloudflare.com",
             "https://www.github.com"]
    for site in sites:
        try:
            requests.get(site, timeout=5)
            return True
        except:
            continue
    return False


def write_log(status):
    time_now = datetime.now().strftime("%Y-%m-%d%H:%M:%S")
    with open("log.txt", "a") as file:
        file.write(f"{time_now} - {status}\n")


if __name__ == "__main__":
    if check_internet():
        message = "internet connected"
    else:
        message = "internet disconnected"
    print(message)
    write_log(message)
