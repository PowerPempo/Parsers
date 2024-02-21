import requests
from bs4 import BeautifulSoup as BS

def parse_ssr():
    response = requests.get('https://coinmarketcap.com/')
    soup = BS(response.content , 'html.parser')
    data = soup.find('a' , {'href': "/currencies/tether/#markets"}).text
    return data

if __name__ == '__main__':
    print('Tether rate is: ' , parse_ssr())