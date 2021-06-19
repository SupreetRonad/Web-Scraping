import bs4
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
res = requests.get('https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi', headers=headers)

soup = bs4.BeautifulSoup(res.text, 'lxml')

title = soup.select('.filter-pro-info')
for i in soup.select('.filter-pro-info'):
    temp = i.select('.property-price')
    print(temp[0].text) 
    print('\n ########################## \n')

