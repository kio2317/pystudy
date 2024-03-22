import requests # pip install requests 사용
from bs4 import BeautifulSoup # 뷰티플 숲 사용 검색 하기
import pyautogui # pip install pyautogui

#key word 함수 안에 input함수로 입력 가능
keyword = pyautogui.prompt("검색어를 입력하세요. ")
lastpage = pyautogui.prompt("마지막 페이지 입력해 주세요.")
pageNum = 1
for i in range(1, int(lastpage) * 10,10):
  print(f"{pageNum}페이지입니다.========================================")
  respones =requests.get(f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}$start={i}")

  html = respones.text
  soup = BeautifulSoup(html, 'html.parser')
  links = soup.select(".news_tit") 

  for link in links:
    title = link.text # 태그 안에 텍스트 요소를 가져온다.
    url = link.attrs['href'] #href의 속성 값을 가져온온다.
    print(title, url)
    pageNum= pageNum + 1