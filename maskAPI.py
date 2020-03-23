import requests
import json
import sys

url="https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1"

print("마스크의 재고가 남아 있는 판매처의 정보가 출력됩니다.")
print("주소를 입력해주세요. (시군구의 정보가 필요합니다.)")

Inp=input()

r=requests.get(url+"/storesByAddr/json?address="+Inp)
sales=json.loads(r.text)["stores"]

for s in sales:
    if ("remain_stat" not in s):
        continue
    
    if (s["remain_stat"]!="empty") and (s["remain_stat"]!="break"):
        print(s)
