from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동 업데이트
#improt
import time
import pyautogui
import pyperclip

#꺼짐 방지 코드
Chrome_options = Options()
Chrome_options.add_experimental_option("detach", True)

# 불필요한 에러 메시지 없애기
Chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=Chrome_options)

# 웹 페이지 주소이동
driver.implicitly_wait(5) # 웹 페이지가 로딩 될때까지 5초 기다림
driver.maximize_window() # 화면 최대화 
driver.get("https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/")

# 아이디 입력창
id = driver.find_element(By.CSS_SELECTOR, "#id")
id.click() # 아이디 클릭
pyperclip.copy("kio2317")
pyautogui.hotkey("ctrl", "v")
time.sleep(2) # 2초뒤 

# 비밀번호  입력창
pw = driver.find_element(By.CSS_SELECTOR, "#pw")
pw.click()
pyperclip.copy("wodnjs47520@")
pyautogui.hotkey("ctrl", "v")
time.sleep(2)

#로그인 버튼
login_btn = driver.find_element(By.CSS_SELECTOR, "#log\.login")
login_btn.click()