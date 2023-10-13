import requests

for i in range(1,11):
    print('page:',i)
    url = f'https://quotes.toscrape.com/page/{i}/'
    r= requests.get(url)
    html = r.text
    with open('authors_quotes.csv','a', encoding='utf-8') as f:
        for line in html.split('\n'):
            if '<span class="text" itemprop="text">' in line:
                quotes = line.replace('<span class="text" itemprop="text">“','').replace('”</span>','')
                quotes = quotes.strip()
                # print(quotes)

            if '<small class="author" itemprop="author">' in line:
                author = line.replace('<span>by <small class="author" itemprop="author">', '').replace('</small>', '')
                author = author.strip()
                # print(author)
                # print(author+","+quotes)
                f.write(author+','+quotes)
                f.write('\n')