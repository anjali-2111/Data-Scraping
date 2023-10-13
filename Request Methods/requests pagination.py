import requests

for i in range(1,11):
    print('page:',i)
    url = f'https://quotes.toscrape.com/page/{i}/'
    r= requests.get(url)
    html = r.text
    with open('quotes1.txt','a', encoding='utf-8') as f:
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                line = line.replace('<span class="text" itemprop="text">“','').replace('”</span>','')
                line = line.strip()
                f.write(line)
                f.write('\n')