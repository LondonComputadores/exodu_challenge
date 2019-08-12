import requests
from bs4 import BeautifulSoup
import csv

r = requests.get("https://reports.exodus-privacy.eu.org/en/trackers/", params=dict({
                  "name":"h1", "url":"p", "code_detection_rule":"li", "network_detection_rule":"li",
                   "about":"p", "ownership":"p", "what_it_does":"ul", "data_policy":"li"}))

soup = BeautifulSoup(r.text, 'html.parser')

r_info = ["name", "url", "code_detection_rule", "network_detection_rule",
               "about", "ownership", "what_it_does", "data_policy"]
with open("/c/Users/londo/Documents/psafe_challenge/rep_exodus_challenge/exodu_challenge/param_output.csv", "w") as f:
    writer = csv.DictWriter(f, r_info) 

print(r_info)
