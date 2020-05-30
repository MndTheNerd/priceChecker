import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/ASUS-i7-10510U-Innovative-ScreenPad-UX481FL-XS74T/dp/B083Z8K6D9/ref=sr_1_3?dchild=1&keywords=zenbook&qid=1590808288&s=specialty-aps&sr=1-3'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id="productTitle")

print(title)
