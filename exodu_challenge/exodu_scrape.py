import requests
from bs4 import BeautifulSoup
import csv

r = requests.get('https://reports.exodus-privacy.eu.org/en/trackers/')

soup = BeautifulSoup('r.text', 'html.parser')

links = soup.find_all('a')

for link in links:
    if "Trackers" in link.text:
        print(link)
        print(link.attrs['href'])

#info_names = ["name", "url", "code_detection_rule", "network_detection_rule",
#               "about", "ownership", "what_it_does", "data_policy"]
with open("/c/Users/londo/Documents/psafe_challenge/rep_exodus_challenge/exodu_challenge/output1.csv", "w") as f:
        writer = csv.DictWriter(f, links)

