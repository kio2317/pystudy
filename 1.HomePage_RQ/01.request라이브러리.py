# 라이브러리 Request 요청하기

import requests

# 홈페이지 요청
response = requests.get("https://www.naver.com/")

# html 함수에 요청한 텍스트 넣기 -> 출력
html = response.text
print(html)