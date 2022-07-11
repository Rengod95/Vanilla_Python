import json
import time
from urllib.request import urlretrieve

with open("./stack_data_from_jumpit_with_company_id_and_img.json",'r') as f:
    data = json.load(f)

stack_img_urls = data['stack_img']
company_img_urls = data['company_img']

count = 0

for stack_key in stack_img_urls.keys():
    count += 1
    if count%10 == 0:
        print(str(count)+"/"+str(len(stack_img_urls.keys())))
    
    if '/' in stack_key:
        file_name = stack_key.replace('/','_')
    else:
        file_name = stack_key    

    urlretrieve(stack_img_urls[stack_key], "./img_stack/"+file_name+".png")
    time.sleep(0.5)

count = 0
for company_key in company_img_urls.keys():
    if count < 1200:
        count += 1
        continue
    else:
        print(company_img_urls[company_key])
        count += 1

        #1088번 회사 모픽이 회사 이미지를 막아놓음 따라서 try로 끊기지 않도록 변경
        try: 
            if count%10 == 0:
                print(str(count)+"/"+str(len(company_img_urls.keys())))

            if '/' in company_key:
                file_name = company_key.replace('/','_')
            else:
                file_name = company_key 

            urlretrieve(company_img_urls[company_key], "./img_company/"+file_name+".png")
            time.sleep(0.5)

        except:
            pass


