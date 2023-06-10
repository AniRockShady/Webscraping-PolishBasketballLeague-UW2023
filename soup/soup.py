import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import os
import time
new_directory = '/Users/olix/Desktop/UW'
start_time = time.time()
limit = False
url = "https://1lm.pzkosz.pl/zawodnicy.html?fbclid=IwAR2fPt1G4bFrrgC3Zja73pEaoYUPWBp3AqKo4CpNErl0Ot4Nzvh8h5UT-RE"
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

player_links = []

player_items = soup.find_all('div', class_='playersonlist col-xl-3 col-lg-3 col-md-4 col-sm-6')
base_url = "https://1lm.pzkosz.pl"  # Base URL of the website

for i, item in enumerate(player_items):
    link = item.find('a')
    full_url = urljoin(base_url, link['href'])
    player_links.append(full_url)
    if i == 99:
        limit = True
        break


d = pd.DataFrame({'Name': [],'Paszport': [], 'Urodzony': [], 'Wzrost': [], 'Pozycja': [], 'Last team played': [], 'Year': []})
for link in player_links:
    response = requests.get(link)
    player_html = response.content
    player_soup = BeautifulSoup(player_html, 'html.parser')

    try:
       name = player_soup.find('h1').text.strip()
    except:
        name = ''
    try:
        paszport = player_soup.find('span', itemprop='nationality').text.strip()
    except:
        paszport = ''

    try:
        urodzony  = player_soup.find('span', itemprop='birthDate').text.strip()
    except:
        urodzony = ''
    try:
        wzrost = player_soup.find('span', itemprop='height').text.strip()
    except:
        wzrost = ''
    try:
        pozycja = player_soup.find('span', itemprop='roleName').text.strip()
    except:
        pozycja = ''
    try:
        h3_element = player_soup.find('h3', string='Kariera zawodnika w Polsce')
        ul_element = h3_element.find_next('ul')
        li_element = ul_element.find('li')

        year_team_text = li_element.text.strip()

        split_values = year_team_text.split('-', 1)
        year, last_team_played = split_values[0].strip(), split_values[1].strip()
    except:
        year = ''
        last_team_played = ''
    player = {'Name': name,'Paszport': paszport, 'Urodzony': urodzony, 'Wzrost': wzrost, 'Pozycja': pozycja, 'Last team played': last_team_played, 'Year': year}

    d = d.append(player, ignore_index=True)

print(d)
d.to_csv('players.csv')
end_time = time.time()
execution_time = end_time - start_time
print(f"Scraping execution time: {execution_time} seconds")



