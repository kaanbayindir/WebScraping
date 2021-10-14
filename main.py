import time
from bs4 import BeautifulSoup
import requests


def read_reports():
    html_text = requests.get('https://www.haberler.com/son-dakika/').text
    soup = BeautifulSoup(html_text, 'lxml')
    reports = soup.find_all('div', class_='hblnBox')
    for report in reports:
        try:
            time = report.find('div', class_='hblnTime').text
            link = report.a['href']
            title = report.find('a', class_ = 'hblnTitle').text
            info = report.find('div', class_= 'hblnContent').p.text
            print(f"{time.strip()}\n")
            print(f"{title.strip()}\n")
            print(f"{info}\n")
            print(f"{link}\n")
        except:
            pass


if __name__ == '__main__':
    while True:
        read_reports()
        time_wait = 10
        print(f'Waiting {time_wait} minutes...')
        time.sleep(time_wait * 300)
