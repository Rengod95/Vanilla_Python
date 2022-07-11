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

#카테고리 별 
def search_for_category(num_category):
    driver.get("https://www.jumpit.co.kr/positions?jobCategory="+num_category)

    prev_height = driver.execute_script("return document.body.scrollHeight")

    # 웹페이지 맨 아래까지 무한 스크롤
    while True:
        # 스크롤을 화면 가장 아래로 내린다
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        
        # 페이지 로딩 대기
        time.sleep(2)

        # 현재 문서 높이를 가져와서 저장
        curr_height = driver.execute_script("return document.body.scrollHeight")

        if(curr_height == prev_height):
            break
        else:
            prev_height = driver.execute_script("return document.body.scrollHeight")

    job_selector = 'sc-fKVqWL'
    job_list = driver.find_elements(By.CLASS_NAME, job_selector)
    a_tag_list = []

    for job in job_list :
        a_tag = job.find_element(By.CSS_SELECTOR, 'a')
        href = a_tag.get_attribute('href')

        a_tag_list.append(href)
    
    print(str(num_category) + "번 카테고리의 url을 모두 수집했습니다. 총 " + str(len(a_tag_list)) + "개의 직무를 발견했습니다.")

    return a_tag_list

def get_job_information(url_list,num):
    
    count = 0
    total_length = len(url_list)

    for url in url_list:
        driver.get(url)

        # 페이지 로딩 대기
        time.sleep(1.5)

        job_desc_selector = 'sc-edERGn'
        company_name_selector = 'position_title_box_desc'
        position_tags_selector = 'position_tags'
        stack_tags_selector = 'sc-jlsrNB'
        
        job_info_element = driver.find_element(By.CLASS_NAME, job_desc_selector)
        company_name_element = driver.find_element(By.CLASS_NAME, company_name_selector)

        job_desc = job_info_element.find_element(By.CSS_SELECTOR, 'h1').text
        company_name = company_name_element.find_element(By.CSS_SELECTOR, 'a').text

        position_tags = []
        try :
            position_tags_element = driver.find_element(By.CLASS_NAME, position_tags_selector)
            position_tags_li = position_tags_element.find_elements(By.CSS_SELECTOR, 'li')
            
            for tag_element in position_tags_li:
                position_tags.append(tag_element.find_element(By.CSS_SELECTOR, 'a').text[1:]) # 앞에 '#'은 없앰
        except :
            pass

        stack_tags = []
        try :
            stack_tags_element = driver.find_elements(By.CLASS_NAME, stack_tags_selector)

            for stack_element in stack_tags_element:
                stack_name = stack_element.text
                stack_tags.append(stack_name)
                if stack_name not in stack_img_url.keys():
                    stack_img_url[stack_name] = stack_element.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')
        except :
            pass
        
        final_job_info = {
            'category':JOB_CATEGORIES[num],
            'company_name':company_name,
            'description':job_desc,
            'job_tag':position_tags,
            'stack_tag':stack_tags
        }

        pprint.pprint(final_job_info)
        result.append(final_job_info)
        count += 1
    
        if count%10 == 0:
            print("\n[ ------------ " + str(count)+'/'+str(total_length)+ " 진행도 : " + str(round(count/total_length*100,1)) + "% ------------ ]\n" )
    
    
if __name__ == "__main__":

    JOB_CATEGORIES = {
        '1':"서버/백엔드 개발자",
        '2':"프론트엔드 개발자",
        '3':"웹 풀스택 개발자",
        '4':"안드로이드 개발자",
        '5':"게임 클라이언트 개발자",
        '6':"게임 서버 개발자",
        '7':"DBA",
        '8':"인공지능/머신러닝",
        '9':"devops/시스템 엔지니어",
        '10':"정보보안 담당자",
        '11':"QA엔지니어",
        '12':"개발 PM",
        '13':"HW/임베디드",
        '15':"SW/솔루션",
        '16':"iOS 개발자",
        '17':"웹퍼블리셔",
        '18':"크로스플랫폼 앱개발자",
        '19':"빅데이터 엔지니어",
        '20':"VR/AR/3D",
        '21':"기술지원"
    }

    # 스택 이미지만 따로 모음
    stack_img_url = {}

    # 최종 json으로 변환할 dictionary
    final_result = {}

    #조사한 날짜
    date = str(datetime.datetime.today().strftime("%Y/%m/%d"))
    final_result['date'] = date

    # 결과를 담을 list
    result = []

    # 크롬 드라이버 설정
    chrome_service=Service(ChromeDriverManager().install())
    chromeDriverOptions = webdriver.ChromeOptions()
    chromeDriverOptions.add_argument('--no-sandbox')
    # headless 붙이면 창 없이 실행
    # chromeDriverOptions.add_argument('--headless')
    chromeDriverOptions.add_argument("--disable-notifications")
    chromeDriverOptions.add_argument('--lang=ko-KR')
    chromeDriverOptions.add_argument('--window-size=1920x1080')
    chromeDriverOptions.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='./chromedriver',options=chromeDriverOptions,service = chrome_service)

    # url_list = search_for_category('20')
    # get_job_information(url_list,'20')

    for num in JOB_CATEGORIES.keys():
        print(str(num) + "번 카테고리 - " + JOB_CATEGORIES[num] + "의 직무탐색을 시작합니다.")
        url_list = search_for_category(num)
        get_job_information(url_list,num)

    final_result['result'] = result
    final_result['stack_img'] = stack_img_url

    with open('./stack_data_from_jumpit.json','w') as f:
        json.dump(final_result, f, ensure_ascii=False, indent=4)
    
    pprint.pprint(final_result)
    
    