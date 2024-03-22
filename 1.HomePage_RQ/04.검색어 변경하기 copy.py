import requests # pip install requests 사용
from bs4 import BeautifulSoup # 뷰티플 숲 사용 검색 하기
import pyautogui # pip install pyautogui

#key word 함수 안에 input함수로 입력 가능
keyword = pyautogui.prompt("검색어를 입력하세요. ")
# URL에서 keyword함수를 받로록 설정 | uer에서 f{ }스트링 자연스레 연결 가능
respones =requests.get(f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}")

html = respones.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select(".news_tit") 

for link in links:
  title = link.text # 태그 안에 텍스트 요소를 가져온다.
  url = link.attrs['href'] #href의 속성 값을 가져온온다.
  print(title, url)