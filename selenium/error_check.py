import os
import json

with open("./stack_data_from_jumpit_with_company_id_and_img.json",'r') as f:
    data = json.load(f)

company_img_urls = data['company_img']

file_list = os.listdir('./img_company/')
file_name_list = []
for file_name in file_list:
    file_name_list.append(file_name.split('.')[0])

for i in company_img_urls.keys() :
    if i not in file_name_list :
        print("file not containing :")
        print(i)

# 1088번 모픽은 회사 이미지 엑세스 막아놓음