from selenium import webdriver

# Keys = enter, ecs를 입력하고 싶을 때
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# 복붙
import pyperclip

# chrome 내부에 정보 남기는용
from selenium.webdriver.chrome.options import Options

# .env 사용하려고 할 때
from dotenv import load_dotenv
import os

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

# .env file load
load_dotenv()

optionTest = webdriver.ChromeOptions()
# user-data-dir 앞에 -- 꼭 넣어줘야 함
optionTest.add_argument(r'--user-data-dir=/Users/azullcarrot/Library/Application Support/Google/Chrome/Default')

driver = webdriver.Chrome(options=optionTest)
driver.get('https://nid.naver.com/nidlogin.login?svctype=262144')

# notebook 환경에서는 wifi로 인해서 느릴 수 있으니 3초 지연주는 것이 안정적
# time.sleep(3)
# 혹은 implicitly wait 사용해서 요소가 나올 때까지 10초 동안 기다리도록 설정
driver.implicitly_wait(10)

# id .env에서 훔쳐오기
pyperclip.copy(os.getenv('id'))

id = driver.find_element(By.CSS_SELECTOR, '#id')
id.send_keys(Keys.COMMAND, 'v')

time.sleep(1)

# pw .env에서 훔쳐오기
pyperclip.copy(os.getenv('pw'))

pw = driver.find_element(By.CSS_SELECTOR, '#pw')
pw.send_keys(Keys.COMMAND, 'v')

time.sleep(1)

pw.send_keys(Keys.ENTER)

# blog post move step 1
driver.get('https://section.blog.naver.com/BlogHome.naver?directoryNo=0&currentPage=1&groupId=0')

driver.implicitly_wait(10)

# blog post move step 2
driver.get(f'https://blog.naver.com/{os.getenv("id")}?Redirect=Write&')

# post context part
time.sleep(2)

# todo 이거 iframe 안에 있어서 안에서 접근해서 수정하고 빠져나와야 함

# iframe이 있다면 먼저 전환
iframe = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.TAG_NAME, "iframe"))
)
driver.switch_to.frame(iframe)

# 요소 찾기 및 변경
placeholder_span = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//span[contains(text(), '본문에 #을 이용하여 태그를 사용해보세요')]"))
)
driver.execute_script("arguments[0].textContent = '새로운 텍스트 입력됨!';", placeholder_span)

# 다시 원래 페이지로 돌아오기
driver.switch_to.default_content()

# todo type="button" 찾아서 발행해야 함 ㅇㅇ




input('enter')