import json
import requests
url = ("https://www.dcard.tw/service/api/v2/forums/pet/posts?limit=3&before=235778028")
respond = requests.get(url)
jsonData = json.loads(respond.text)
D = {}
for data in jsonData:
    D['title'] = data['title']
    D['topics'] = ['topics']
    D['gender'] = ['gender']
    D['school'] = ['school']

    with open("Dcard.json", 'a', encoding="utf-8") as f:
        json.dump(D, f, ensure_ascii=False)