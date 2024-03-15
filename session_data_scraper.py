import requests
from bs4 import BeautifulSoup

# Assuming the HTML content is stored in a variable called 'html_content'
url = "https://thesession.org/tunes"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')

# Find all tune listings
tune_listings = soup.find_all('li', class_='manifest-item')

for tune in tune_listings:
    try:
        tune_name = tune.find('a').text.strip()
        tune_detail = tune.find('span', class_='detail').text.strip() if tune.find('span', class_='detail') else 'No detail available'
        contributor = tune.find('a', {'data-memberbio': True}).text.strip() if tune.find('a', {'data-memberbio': True}) else 'No contributor listed'
        time_added = tune.find('time').get('title').strip() if tune.find('time') else 'No time added listed'

        print(f"Tune Name: {tune_name}")
        print(f"Detail: {tune_detail}")
        print(f"Contributor: {contributor}")
        print(f"Time Added: {time_added}")
        print('-' * 50)
    except Exception as e:
        print(f"An error occurred while processing one of the tunes: {e}")
        continue