import requests
from bs4 import BeautifulSoup
import csv

r = requests.get('https://reports.exodus-privacy.eu.org/en/trackers/')

soup = BeautifulSoup(r.text, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))

'''for ul in soup.find_all('ul', class_='container-fluid'):
    for li in ul.find_all('li'):
        a = li.find('a')
        print(a['href'], a.get_text())'''

