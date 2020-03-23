import requests
import json

url="https://8oi9s0nnth.apigw.ntruss.com/corona19-masks/v1"

r=requests.get(url+"/storesByAddr/json?address=서울특별시%20서대문구")
sales=json.loads(r.text)["stores"]

for s in sales:
    if ("remain_stat" not in s):
        continue
    
    if (s["remain_stat"]!="empty") and (s["remain_stat"]!="break"):
        print(s)
