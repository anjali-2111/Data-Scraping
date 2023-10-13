# Hands on with Requests
# server brower communication

import requests

r =requests.get("https://quotes.toscrape.com/")
print(r.status_code)
# print(r.text)


html = r.text

with open('authors.txt','w') as f:
    for line in html.split('\n'):
        if '<small class="author" itemprop="author">' in line:
            line = line.replace('<span>by <small class="author" itemprop="author">','').replace('</small>','')
            f.write(line)
            f.write('\n')