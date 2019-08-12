import requests
from bs4 import BeautifulSoup
import csv


all_trackers = []
url = ('https://reports.exodus-privacy.eu.org/en/trackers/')
data = requests.get(url)
html = BeautifulSoup(data.text, 'html.parser')
link = html.selector('ul li.col-lg-6')
for tracker in trackers:
    tracker_class = tracker['div-class']
    tracker_text = tracker.select('p.tracker-text')[0].get_text()
    all_trackers.append({"name": "h1", "url": "p", "code_detection_rule": "li", "network_detection_rule": "li",
                          "about": "p", "ownership": "p", "what_it_does": "ul", "data_policy": "li"})
    print(all_trackers)