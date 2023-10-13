import requests
import json

with open('headlines.csv','w') as f:
    for i in range(1,3):
        print("page:",i)
        url = f"https://www.espncricinfo.com/ci/content/story/data/index.json?genre=706;;page={i}"
        r = requests.get(url)
        html = json.loads(r.text)
        for headlines in html:
            headline = headlines['headline']
            headline = headline.replace(',','|')
            f.write(headline)
            f.write('\n')