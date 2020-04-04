import requests
from bs4 import BeautifulSoup

def query(queryList, userQuery):

    cardList = queryList
    url = 'https://shop.tcgplayer.com/productcatalog/product/show?'


    payload = {
        'NewSearch' : 'false',
        'ProductTyple' : 'All',
        'IsProductNameExact' : 'true',
        'ProductName': userQuery
    }
    r =requests.post(url, params=payload).text
    source = BeautifulSoup(r, 'lxml')
    conditions = source.find_all('div', class_='listing__condition')
    prices = source.find_all('div', class_='listing__pricing')

    for card in range(len(conditions)):
        con = conditions[card].text
        con = con.replace('\n', ' ')
        pri = prices[card].text
        pri = pri.replace('\n', ' ')
        details = con, pri
        cardList.append(details)
    return(cardList)
