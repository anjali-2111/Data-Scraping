# Hands on with Requests
# server brower communication
import requests
r= requests.get("https://quotes.toscrape.com/")

print(r.status_code)

# parse the text
# r.encoding
# print(r.text)
# print(r.headers)

# r = requests.get("https://help.netflix.com/en/node/2064")
# print(r.status_code)
# print(r.headers)
# print(r.text)

html = r.text

with open('quotes.txt','w') as f:
    for line in html.split('\n'):
        if '<span class="text" itemprop="text">' in line:
            line = line.replace('<span class="text" itemprop="text">“','').replace('”</span>','')
            line = line.strip()
            f.write(line)
            f.write('\n')