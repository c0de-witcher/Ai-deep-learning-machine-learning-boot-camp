import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://en.wikipedia.org/wiki/India',
    'https://en.wikipedia.org/wiki/United_Kingdom',
    'https://en.wikipedia.org/wiki/United_States'
]

def fetch_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Title of {url}: {soup.title.string}")
    print(f"fetched {len(soup.text)} characters from {url}")

threads =[]

for url in urls:
    thread = threading.Thread(target=fetch_url , args= (url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.joim()

print("All threads have finished execution.")