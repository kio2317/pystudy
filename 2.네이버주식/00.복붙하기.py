import requests 
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/sise.naver?code=000660"
response = requests.get(url)
html = response.text
soup =BeautifulSoup(html, 'html.parser')
soup.select_one("#_nowVal")
