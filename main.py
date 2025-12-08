import requests
from bs4 import BeautifulSoup
import csv

def main():
    total_pages = 1
    url = "https://www.gamespot.com/news/?page="

    with open('gamespot_news.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['title', 'link', 'image_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for page_number in range(total_pages):
            response = requests.get(f"{url}{page_number}")
            soup = BeautifulSoup(response.text, "lxml")
            for card in soup.select(".card-item"):
                img = card.select_one(".card-item__img").select_one("img").get("src")
                link = card.select_one(".card-item__link").get("href")
                title = card.select_one(".card-item__title").get_text(strip=True)

                writer.writerow({
                    'title': title,
                    'link': f"https://www.gamespot.com{link}",
                    'image_url': img
                })

if __name__ == "__main__":
    main()
