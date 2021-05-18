#!/usr/bin/env python3

import csv
import requests
from bs4 import BeautifulSoup

base_url = 'https://www.cse.iitb.ac.in/page222'
writer = csv.writer(open('count.csv', 'w'))
writer.writerow(['Category Name', 'No. of students'])
cse_page = BeautifulSoup(requests.get(base_url).text, 'html.parser')

for a in cse_page.find_all('a', href=True):
    if a['href'][:7] == '?batch=':
        batch_page = BeautifulSoup(requests.get(base_url + a['href']).text, 'html.parser')
        name = batch_page.find(attrs={'class': 'mpart'}).h1.text
        rows = sum(len(batch_page.find_all(attrs={'class': row})) for row in ['row1', 'row2'])
        writer.writerow([name, rows])
