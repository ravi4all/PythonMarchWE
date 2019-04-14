import bs4
import urllib.request as url

http = url.urlopen('https://timesofindia.indiatimes.com/')
#print(http)
#lxml - library xml
webpage = bs4.BeautifulSoup(http, 'lxml')
#print(webpage)
story = webpage.find('ul', class_='list8')
#print(story)
a = story.find_all('a')
#print(a)
for link in a:
    print(link.text)
