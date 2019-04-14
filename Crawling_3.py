import bs4
import urllib.request as url

toSearch = input("Enter movie name : ")
http = url.urlopen("https://www.imdb.com/find?ref_=nv_sr_fn&q="+toSearch)
page = bs4.BeautifulSoup(http, 'lxml')

td = page.find('td', class_='result_text')
href = td.find('a')['href']

newUrl = "https://www.imdb.com"+href
#print(newUrl)

newResponse = url.urlopen(newUrl)
newPage = bs4.BeautifulSoup(newResponse, 'lxml')
title = newPage.find('div', class_='title_wrapper')
title = title.text
title = title.replace('\n','')
title = title.split()
#print(title)
print(' '.join(title))

summary = newPage.find('div', class_='summary_text')
summary = summary.text.strip()
print(summary)
