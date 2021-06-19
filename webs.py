import bs4
import requests
import xlsxwriter     
      
book = xlsxwriter.Book('Example2.xlsx')     
sheet = book.add_sheet()   

'''
property-location
property-price
price-per-unit
area
facing
status
owner/agent name
posted
'''
def scrap():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
    }
    res = requests.get(
        'https://www.propertiesguru.com/residential-search/2bhk-residential_apartment_flat-for-sale-in-new_delhi', headers=headers)

    soup = bs4.BeautifulSoup(res.text, 'lxml')

    title = soup.select('.filter-pro-info')
    for i in soup.select('.filter-property-list'):
        # temp = i.select('.filter-pro-heading')[0]
        location = i.find('span').get_text(strip=True)
        price = i.find('span', class_='price').get_text(strip=True)
        ppu = i.find('span', class_='price-per-unit').get_text(strip=True)
        area = i.find('div', class_='col-4').get_text(strip=True)[4::]
        facing = i.select(
            '.filter-pro-details')[0].find('div', class_='col-3').getText(strip=True)[6::]
        status = i.find('div', class_='col-5').get_text(strip=True)[6::]
        temp = i.find(class_='pro-list')
        floor = str(temp).split('<li>')[1].split(' ')[0]
        floor = floor[:len(floor) - 2:]

        furnish = str(temp).split('<li>')[2].split('</li>')[0]
        hold = str(temp).split('<li>')[3].split('</li>')[0]
        bathroom = str(temp).split('<li>')[4].split('</li>')[0].split(' ')[0]

        owner = i.find('span', class_='owner-name').get_text(strip=True)
