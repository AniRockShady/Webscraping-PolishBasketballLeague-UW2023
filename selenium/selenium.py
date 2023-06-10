from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import pandas as pd
from time import sleep, time

options = FirefoxOptions()
driver = webdriver.Firefox(options=options, executable_path='/snap/bin/geckodriver')

# The target URL
url = 'https://1lm.pzkosz.pl/zawodnicy.html'

# Page request
start_time = time()
driver.get(url)

# Page source
html = driver.page_source

# BeautifulSoup object and the parser
soup = BeautifulSoup(html, 'html.parser')

# Finding all divs that contain player info
players_divs = soup.find_all('div', {'class': 'playersonlist col-xl-3 col-lg-3 col-md-4 col-sm-6'})

# Storing player data as a list
players = []

# Loop over each div and scrape the player's name and link
for div in players_divs:
    link_tag = div.find('a')  # find the 'a' tag inside the div
    player_name = link_tag.text.strip()  # get the player's name
    player_link = 'https://1lm.pzkosz.pl' + link_tag['href']  # get the player's link
    players.append((player_name, player_link))

# Dataframe to store all players' details
df = pd.DataFrame(columns=['Name', 'Paszport', 'Urodzony', 'Wzrost', 'Pozycja', 'Last Team'])

# Loop over each player link and scrape player details
for index, (player, link) in enumerate(players):
    if index == 100:  # Stop after scraping 100 players
        break

    # Navigating player page
    driver.get(link)
    sleep(1)  # Add a delay to respect the website's resources

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # Finding the div that contains player info
    player_info_div = soup.find('div', {'class': 'col-xl-3 col-lg-4 col-md-6 col-sm-12 mycol'})

    # Finding all divs that contain player details
    player_details_divs = player_info_div.find_all('div', {'class': 'row align-items-center'})

    # Dictionary to store player details
    player_details = {'Name': player}

    # Loop over each div and scrape the player detail
    for div in player_details_divs:
        detail_name = div.find('div', {'class': 'col-6'}).text.strip().replace(':', '')  # get the detail name and remove the colon
        detail_value = div.find('div', {'class': 'col-6 numer'}).text.strip()  # get the detail value
        player_details[detail_name] = detail_value

    try:
        player_career_div = soup.find('div', {'class': 'col-xl-6 col-lg-6 col-md-6 col-sm-12 mycol'})
        career_details_ul = player_career_div.find('ul')
        last_team = career_details_ul.find('li').text.strip()
        player_details['Last Team'] = last_team
    except AttributeError:
        player_details['Last Team'] = 'N/A'  # default value if the last team is not present

    for column in df.columns:
        player_details[column] = player_details.get(column, 'N/A')

    print(player_details)

    # Adding the player details to the dataframe
    df = df.append(player_details, ignore_index=True)

end_time = time()  # end time

driver.quit()

print(df)

print(f"Execution time: {end_time - start_time} seconds")

df.to_csv("players.csv", index=False)
