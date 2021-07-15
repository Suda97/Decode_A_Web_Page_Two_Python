import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    base_url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
    source = requests.get(base_url)
    soup = BeautifulSoup(source.text, 'html.parser')
    all = soup.find_all("p", {"class": "has-dropcap"}) + soup.find_all("p", {"class": "paywall"})

    for elem in all:
        print(elem.text)
