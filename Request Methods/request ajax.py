import requests
import json


# print(r.text)
# print(type(r.text))
# print(html)
# print(type(html))

with open('news.txt','w') as f:
    for i in range(0, 11):
        print('page:', i)
        url = f"https://www.espncricinfo.com/ci/content/story/data/index.json?;type=7;page={i}"
        r = requests.get(url)
        html = json.loads(r.text)
        for news in html:
            res = news['author']+" | "+news['summary']
            f.write(res)
            f.write('\n')
