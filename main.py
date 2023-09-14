from bs4 import BeautifulSoup
import requests
from NotifManager import NotifManager

PRODUCT_URL = "https://www.amazon.in/gp/product/B08CFSZLQ4/?&tag=siteplug658205-21"
THRESHOLD = 30000.0
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/97.0.4692.71 Safari/537.36 "
}

response = requests.get(url=PRODUCT_URL, headers=headers)
amazon_webpage = response.text
amazon_soup = BeautifulSoup(amazon_webpage, "html.parser")
price_soup = amazon_soup.find(name="span", class_="a-offscreen")
product_soup = amazon_soup.find(name="span", id="productTitle", class_="a-size-large product-title-word-break")
product_name = product_soup.getText()

price_val = price_soup.getText().split("₹")[1].split(".")[0].split(",")
price_val = float(price_val[0] + price_val[1])

if price_val < THRESHOLD:
    print(f"Offer Available! {product_name} available @ ₹{price_val}!")
    notification = NotifManager()
    notification.send_notif(price_val, THRESHOLD, product_name)
else:
    print("No offer available yet!")
