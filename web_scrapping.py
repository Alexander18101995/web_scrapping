import requests
import bs4 
from headers import headers
response = requests.get('https://habr.com/ru/all/',headers=headers)
text = response.text
HUBS = {'Научно-популярное'}
soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all(class_='tm-article-snippet')
for articl in articles:
  hubs = articl.find_all(class_='tm-article-snippet__hubs-item')
  hubs = {hub.find('a').text.strip() for hub in hubs}
  if hubs & HUBS:
    art_time = articl.find('time')
    art = articl.find('h2').find('a')
    href = art.attrs['href']
    url = 'https://habr.com' + href 
    print(art_time.text,art.text, '--->', url)
    print('-----------')
