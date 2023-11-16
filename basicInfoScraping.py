from bs4 import BeautifulSoup
import requests

url = 'https://scrapingclub.com/exercise/detail_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='my-8 w-full rounded border')

for item in items:
    itemName = item.find('h3', class_='card-title').text
    itemPrice = item.find('h4', class_='my-4 card-price').text
    itemDesc = item.find('p', class_='card-description').text
print('Great {} is avaliavle for price {}, see details: {}'.format(itemName, itemPrice, itemDesc))

