import requests 
from bs4 import BeautifulSoup
import openpyxl

fpath = r'C:\Users\kio23\Desktop\front\py_rolli\2.네이버주식\주식데이터.xlsx'

wb = openpyxl.load_workbook(fpath)
ws = wb.active # 현재 활성화된 시트를 선택

# 종목 코드 리스트
codes = [
  '000660',
  '005930',
  '035720',
  '377300'
]

row= 2
for code in codes:
  url = f"https://finance.naver.com/item/sise.naver?code={code}"
  response = requests.get(url)
  html = response.text
  soup =BeautifulSoup(html, 'html.parser')
  price = soup.select_one("#_nowVal").text
  price =price.replace(',','') # , 없애기

  print(price)
  ws[f'B{row}'] = int(price)
  row = row +1 

wb.save(fpath)