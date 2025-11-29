import requests
from bs4 import BeautifulSoup

def main():
    url = "https://www.gamespot.com/news/"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "lxml")

    for card in soup.select(".card-item"):
            img = card.select_one(".card-item__img").select_one("img").get("src")
            link = card.select_one(".card-item__link").get("href")
            title = card.select_one(".card-item__title").get_text(strip=True)

            print(str(link))
            print(str(title))
            print(str(img))
            print()

if __name__ == "__main__":
    main()
