import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.naver.com/")
html = response.text
soup =BeautifulSoup(html, 'html.parser')
word =soup.select_one('#header')


print(word.text)

# 태그를 이름으로 가져오기 <h1> <a>
# id = # 붙여서 가져오기 ex #header
# class =.을 붙여 가져오기 -> .info_gruop
#  내가 원하는 태그에 별명없을때 -> 클레스 > 아래태그 ex .logo_gruop > span 