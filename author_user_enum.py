import requests
from bs4 import BeautifulSoup

url = "https://example.com/?author=2"

headers = {
    "Host": "example.com",
    "Sec-Ch-Ua": '"Chromium";v="131", "Not_A Brand";v="24"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Linux"',
    "Accept-Language": "en-US,en;q=0.9",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.86 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=0, i"
}

base_url = "https://example.com/?author="

for i in range(1, 10000):
    url = f"{base_url}{i}"
    response = requests.post(url, headers=headers)

    print(f"Trying author={i} - Status: {response.status_code}")

    if response.status_code == 404:
        print("404 Not Found. Stopping.")
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    meta_tag = soup.find("meta", attrs={"property": "og:title"})

    if meta_tag:
        print(f"[author={i}] {meta_tag}")
    else:
        print(f"[author={i}] No og:title found.")
