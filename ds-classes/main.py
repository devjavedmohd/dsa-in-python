from selenium import webdriver # pip install selenium
from selenium.webdriver.chrome.options import Options
from notifypy import Notify
import os
from bs4 import BeautifulSoup # pip install beautifulsoup4
from datetime import datetime

def get_data():
    options = Options()
    # options.add_argument("--headless") # chrome won't visible
    # options.add_argument("--proxy-server=gate.nodemaven.com:8080")

    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

    with open("products.txt") as f:
        products = f.readlines()
        
    driver = webdriver.Chrome(options=options)

    i = 0
    for product in products:
        driver.get(product)
        i += 1
        page_source = driver.page_source
        with open(f"data/{i}.html", "w", encoding="utf-8") as f:
            f.write(page_source)

def extract_data():
    files = os.listdir("data")
    for file in files:
        print(file)
        with open(f"data/{file}", encoding="utf-8") as f:
            content = f.read()

        soup = BeautifulSoup(content, 'html.parser')
        title = soup.title.getText().split(":")[0]
        
        time = datetime.now()
        
        price = soup.find(class_="a-price-whole")
        priceInt = price.getText().replace('.', '').replace(',','')
        table = soup.find(id = "productDetails_detailBullets_sections1")
        asin = table.find(class_="prodDetAttrValue").getText().strip()
        
        print(priceInt, asin, title, time)
        
        with open("finaldata.txt", "a") as f:
            f.write(f"{priceInt}~~{asin}~~{title}~~{time}\n")


if __name__ == "__main__":
    notification = Notify()
    notification.title = "Extracting Data"
    notification.message = "Extracting data from Amazon."
    notification.send()

    get_data()
    extract_data()



class PlayerCharacter:
    def __init__(self, name, health, mana, level):
        self.name = name
        self.health = health
        self.mana = mana
        self.level = level

    def attack(self):
        print(f"{self.name} is attacking.".capitalize())

    def heal(self):
        print(f"{self.name} is healing.")

    def level_up(self):
        self.level += 1
        print(f"{self.name} is leveling up to level {self.level}.")