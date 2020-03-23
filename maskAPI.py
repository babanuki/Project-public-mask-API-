import requests
import json
import sys

url="https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1"

print("마스크의 재고가 남아 있는 판매처의 정보가 출력됩니다.")
print("주소를 입력해주세요. (시군구의 정보만 필요합니다.)")

Inp1=input()

print("혹시 동 혹은 도로명에 대한 정보가 있다면, 해당 정보도 반영해드리겠습니다.")

Inp2=input()

r=requests.get(url+"/storesByAddr/json?address="+Inp1)
sales=json.loads(r.text)["stores"]

cnt=0

for s in sales:    
    if ("remain_stat" not in s):
        continue

    if (Inp2 not in s["addr"]):
        continue
    
    if (s["remain_stat"]!="empty") and (s["remain_stat"]!="break") and (s["remain_stat"]!="None"):
        cnt+=1

        print(str(cnt)+")")
        
        for elem in s:
            print(elem + " : " + str(s.get(elem)))

        print()

if cnt==0:
    print("주소 정보가 잘못되었거나, 혹은 마스크 재고가 남은 판매처가 없습니다.")
