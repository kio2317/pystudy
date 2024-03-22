import requests 
from bs4 import BeautifulSoup

# 종목 코드 리스트
codes = [
  '000660',
  '005930',
  '035720',
  '377300'
]

for code in codes:
  url = f"https://finance.naver.com/item/sise.naver?code={code}"
  response = requests.get(url)
  html = response.text
  soup =BeautifulSoup(html, 'html.parser')
  price = soup.select_one("#_nowVal").text
  price =price.replace(',','') # , 없애기

  print(price)