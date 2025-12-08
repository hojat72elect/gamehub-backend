import requests
from bs4 import BeautifulSoup

def main():
    total_pages = 20
    url = "https://www.gamespot.com/news/?page="

    for page_number in range(total_pages):
        response = requests.get(f"{url}{page_number}")
        soup = BeautifulSoup(response.text, "lxml")
        for card in soup.select(".card-item"):
            img = card.select_one(".card-item__img").select_one("img").get("src")
            link = card.select_one(".card-item__link").get("href")
            title = card.select_one(".card-item__title").get_text(strip=True)

            print(f"https://www.gamespot.com{str(link)}")
            print(str(title))
            print(f"{str(img)}\n")


if __name__ == "__main__":
    main()
