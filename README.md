# Webscraping-PolishBasketballLeague-UW2023
Web scraping project on Polish Basketball League players, conducted by Hande Demirci, Antoni Piotrowski, and Aleksandra Wiśniewska.
# Selenium:
Setting up the Environment: The program begins by importing necessary libraries and setting up the WebDriver options for Firefox. This headless WebDriver automates browser interactions in the background without displaying a graphical user interface.
Accessing the Website: The program then accesses the website specified by the URL. This is done through a GET request that the WebDriver sends to the website's server, emulating the process of a user accessing a website through a browser.
Parsing the HTML: Once the HTML of the webpage is retrieved, it's parsed using BeautifulSoup, a library that converts the HTML into a tree of Python objects. This makes it easy to navigate and search through the HTML structure.
Identifying Data to Scrape: The program identifies all the div elements that contain player information. It then loops over each of these divs and extracts the player's name and link. These data points are appended to a list for further processing.
Collecting Player Details: A pandas DataFrame is created to store all the players' details. The program then loops over each player's link in the list and navigates to the specific webpage of the player. Here, it retrieves the page source and scrapes the player's details, including their name, passport number, date of birth, height, position, and last team. If certain information is not present, the program is built to handle such exceptions gracefully.
Storing Data: The scraped data for each player is added to the DataFrame. This provides a structured format for the data, which is crucial for further analysis and processing.
Timekeeping and Cleanup: The program also keeps track of the total time taken for execution. Once the data scraping is complete, the program cleans up by closing the WebDriver instance.
Saving Data: Finally, the program saves the DataFrame as a CSV file for later use and analysis.
In summary, your program automates the process of data collection from a website. It navigates webpages, identifies and extracts necessary data, organizes the data in a structured format, and saves it for later use, all while keeping track of its execution time.
