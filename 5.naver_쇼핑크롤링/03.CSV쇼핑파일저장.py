from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import csv


#꺼짐 방지 코드
Chrome_options = Options()
Chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
Chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 브라우저 생성
browser = webdriver.Chrome(options=Chrome_options)

#웹 사이트 열기
browser.get('http://www.naver.com')

# 쇼핑메뉴 클릭
#browser.find_element_by_css_selector('a.nav,shop').click()
browser.find_element(By.CSS_SELECTOR, ".service_icon.type_shopping").click()
time.sleep(2)

# 새창을 바라보게 만들기
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

# 화면 최대화 해야지 검색창이 보임
browser.maximize_window()

# 검색창 클릭
search = browser.find_element(By.CSS_SELECTOR, "input._searchInput_search_text_3CUDs")
search.click()

# 검색어 입력
search.send_keys("아이폰14")
search.send_keys(Keys.ENTER)

#스크롤 전 높이
before_h = browser.execute_script("return window.scrollY")

#무한 스크롤(반복문)
while True:
  #맨 아래로 스크롤을 내린다.
  browser.find_element(By.CSS_SELECTOR, "body").send_keys(Keys.END)
  # 스크롤 사이 페이지 로딩 시간
  time.sleep(1)
  #스크롤 후 높이
  after_h = browser.execute_script("return window.scrollY")
  if after_h == before_h:
    break
  before_h =after_h

# 파일 생성
f = open(r"C:\Users\kio23\Desktop\front\py_rolli\원본파일\5.naver_쇼핑크롤링\data.csv",'w',encoding='cp949', newline='')
csvWriter =csv.writer(f)

# list_links=driver.find_elements_by_tag_name('a')
# 상품 정보
items = browser.find_elements(By.CSS_SELECTOR, ".adProduct_info_area__dTSZf")
for item in items:
  name =item.find_element(By.CSS_SELECTOR, ".adProduct_title__amInq").text
  price = item.find_element(By.CSS_SELECTOR, ".adProduct_price__9gODs").text
  link = item.find_element(By.CSS_SELECTOR, ".adProduct_title__amInq > a").get_attribute('href')
  #adProduct_text__8dMZV
  jm = item.find_element(By.CSS_SELECTOR, ".adProduct_text__8dMZV").text
  print(name, price, link)
  csvWriter.writerow([name ,price, link, jm])

#파일 닫기
f.close()