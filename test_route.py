import requests

def check_route(url):
    try:
        response = requests.get(url)
        print(f"URL: {url}")
        print(f"Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error checking {url}: {e}")

check_route("http://127.0.0.1:5000/export/history")
