from bs4 import BeautifulSoup as bs
import requests
from pprint import pprint
import json


def scrap_data(url):
    return requests.get(url)


def main():
    standings_history = []

    for year in range(1950, 2023):
        page_url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'
        page = scrap_data(page_url)
        soup = bs(page.content, 'html.parser')
        archive_table = soup.find('table', attrs={'class': 'resultsarchive-table'})
        tbody = archive_table.find('tbody')
        standings = []
        for row in tbody.find_all('tr'):
            driver_data = {
                'first_name': row.find('span', attrs={'class': 'hide-for-tablet'}).text,
                'last_name': row.find('span', attrs={'class': 'hide-for-mobile'}).text,
                'nationality': row.find('td', attrs={'class': 'dark semi-bold uppercase'}).text,
                'team': row.select('td > a.grey')[0].text,
                'points': row.find('td', attrs={'class': 'dark bold'}).text,
            }
            standings.append(driver_data)
        standings_history.append({f'{year}': standings})
        
    with open('standing.json', 'w') as f:
        json.dump(standings_history, f)
if __name__ == '__main__':
    main()
