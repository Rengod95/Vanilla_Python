from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import json
import time
import pprint
import datetime

# 크롬 드라이버 설정
chrome_service = Service(ChromeDriverManager().install())
chromeDriverOptions = webdriver.ChromeOptions()
chromeDriverOptions.add_argument('--no-sandbox')
# headless 붙이면 창 없이 실행
chromeDriverOptions.add_argument('--headless')
chromeDriverOptions.add_argument("--disable-notifications")
chromeDriverOptions.add_argument('--lang=ko-KR')
chromeDriverOptions.add_argument('--window-size=1920x1080')
chromeDriverOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='./chromedriver', options=chromeDriverOptions, service=chrome_service)


# 컴퍼니 목록이 3808 번 까지 있는 걸 활용해 무차별 대입
def search_for_number(company_number):
    # 스크롤링
    driver.get("https://www.jumpit.co.kr/company/"+str(company_number))
    driver.implicitly_wait(2)
    prev_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)
        curr_height = driver.execute_script("return document.body.scrollHeight")
        if curr_height == prev_height:
            break
        else:
            prev_height = driver.execute_script("return document.body.scrollHeight")

    # 근무 지역 태그의 class name을 이용하여 텍스트 불러오기
    try:
        work_location_selector = ['sc-igXgud', 'sc-JEhMO']
        company_name_selector = 'sc-bSqaIl'

        company_name_element = driver.find_element(By.CLASS_NAME, company_name_selector)
        company_name = company_name_element.find_element(By.CSS_SELECTOR, 'h1').text

        work_location_element = driver.find_element(By.CLASS_NAME, work_location_selector[0])
        work_location_element = work_location_element.find_element(By.CLASS_NAME, work_location_selector[1])
        work_location_element = work_location_element.find_element(By.CSS_SELECTOR, 'ul')
        work_location = work_location_element.find_element(By.CSS_SELECTOR, 'li').text

        location_info = {
            'company_name': company_name,
            'work_location': work_location,
        }
        return location_info
    except:
        pass




if __name__ == "__main__":
    location_result = []
    # 최종 json으로 변환할 dictionary
    final_result = {}
    #조사한 날짜
    date = str(datetime.datetime.today().strftime("%Y/%m/%d"))
    final_result['date'] = date


    for company_number in range(1,3808):
        print(str(company_number) + "번 회사의 근무 장소 탐색을 시작 합니다.")
        location_result.append(search_for_number(company_number))

    final_result['location'] = location_result

    with open('Company_Location.json', 'w') as f:
        json.dump(final_result, f, ensure_ascii=False, indent=4)

    pprint.pprint(final_result)

