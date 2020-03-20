import bs4
import requests

html = requests.get('https://www.dr.dk/radio/programmer')
txt = html.text
soup = bs4.BeautifulSoup(txt, 'html.parser')
events = soup.select('pagination')
print(len(events.get('data-pages')))