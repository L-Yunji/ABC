import requests

url = 'http://127.0.0.1:1080'  # localhost and the defined port + endpoint
body = {"rest_name": "강남역점 홍콩반점0410", "rest_category": "밀집도"}
response = requests.post(url, data=body)
response.json()



'''
import requests
import json

r = requests.post("http://127.0.0.1:5000/predict", json = {"rest_name": "강남역점 홍콩반점0410", 
"rest_category": "밀집도"})
print(r.json())


with open('C:\\Users\\user\\Documents\\rest_data.json', 'rt', encoding='utf-8-sig') as f:
    json_data = json.load(f)

try:
  r = requests.get(BASE, json = json.dumps(json_data, ensure_ascii = False, indent="\t"), verify=False, timeout=5)
  print(r.json())
except requests.exceptions.ConnectionError as e:
    r = "No response"
#except:
  #time.sleep(6)
  #r = requests.get(BASE, json = json.dumps(json_data, ensure_ascii = False, indent="\t"), verify=False)
'''
#try:

'''
try:        
  r = requests.get(BASE, json=  {
    "FIELD1": 2159,
    "rest_name": "강남역점 홍콩반점0410",
    "rest_category": "중국식",
    "rest_number": "02  553 9295",
    "rest_address": "서울특별시 강남구 역삼동 827-4번지 ",
    "rest_location": "[37.4966545, 127.0304097]",
    "rest_rating": 84.59,
    "rest_density": 52.29,
    "rest_recommend": 61.97999999999999
  })
except:
  time.sleep(2)
  requests.get(BASE, json=  {
    "FIELD1": 2159,
    "rest_name": "강남역점 홍콩반점0410",
    "rest_category": "중국식",
    "rest_number": "02  553 9295",
    "rest_address": "서울특별시 강남구 역삼동 827-4번지 ",
    "rest_location": "[37.4966545, 127.0304097]",
    "rest_rating": 84.59,
    "rest_density": 52.29,
    "rest_recommend": 61.97999999999999
  })
    
#for i in range(len())

data = [{"likes": 78, "name": "Tim", "views": 100000},
        {"likes": 10000, "name": "Tim", "views": 80000},
        {"likes": 35, "name": "Tim", "views": 2000}]

for i in range(len(data)):
  response = requests.put(BASE + "video/" + str(i), data[i])
  print(response.json())

input()
response = requests.get(BASE + "video/6")
print(response.json())

'''