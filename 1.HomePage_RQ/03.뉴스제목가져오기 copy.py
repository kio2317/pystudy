import requests
from bs4 import BeautifulSoup

respones =requests.get("https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query=%EC%82%BC%EC%84%B1%EC%A0%84%EC%9E%90")

html = respones.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit")  # 결과테스트 = 이상 없음

for link in links:
  title = link.text # 태그 안에 텍스트 요소를 가져온다.
  url = link.attrs['href'] #href의 속성 값을 가져온온다.
  print(title, url)