import bs4
import urllib.request as url

http = url.urlopen('https://in.bookmyshow.com/national-capital-region-ncr/movies/kesari/ET00063382')
page = bs4.BeautifulSoup(http, 'lxml')
names = page.find('div', class_='synopsis')
print(names.text)
