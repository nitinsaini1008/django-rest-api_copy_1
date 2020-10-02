import json
import requests
url='http://127.0.0.1:8000/api'
data={'id':1,'fields':{'sub':'trial data part 2','num':900}}
ans=requests.get(url,data=json.dumps({}))
print(ans.json())
print(ans.status_code)