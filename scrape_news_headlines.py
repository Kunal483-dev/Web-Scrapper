import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"

response = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"},
    timeout=20
)

response.raise_for_status()

soup = BeautifulSoup(response.text, "html.parser")

headlines = []

for heading in soup.find_all(["h2", "h3"]):
    title = heading.get_text(" ", strip=True)

    if len(title) > 15 and title not in headlines:
        headlines.append(title)

with open("headlines.txt", "w", encoding="utf-8") as file:
    for number, headline in enumerate(headlines, start=1):
        file.write(f"{number}. {headline}\n")

print(f"{len(headlines)} headlines saved in headlines.txt")