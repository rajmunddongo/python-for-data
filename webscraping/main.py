#My first webscrape
from re import sub

from bs4 import BeautifulSoup
import requests
import time

suburl = "https://www.arukereso.hu/videokartya-c3142/asrock/amd-radeon-rx-6950-xt-phantom-gaming-16gb-gddr6-oc-rx6950xt-pg-16go-p944875335/"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
            "cookie": ""}
while True:
    with requests.Session() as s:

        page = s.get(suburl, headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.find("span", {"class" : "name"}).text
        price = int(soup.find("span", {"class": "price"}).text.split('-')[0][:-3].replace(' ',''))
        print(title,price)
        with open("pricelist.txt", "r+") as file:
            # Append to the file instead of overwriting it
            lastPrices = file.readlines()
            if len(lastPrices) != 0:
                lastPrice = lastPrices[-1]
                lastPrice = lastPrice.split(":")[1]
                lastPrice = int(sub(r'[^0-9.]', '', lastPrice))
                if lastPrice < price:
                    file.write(f"{title}:{price}\n")
            else:
                file.write(f"{title}:{price}\n")
        time.sleep(30)
