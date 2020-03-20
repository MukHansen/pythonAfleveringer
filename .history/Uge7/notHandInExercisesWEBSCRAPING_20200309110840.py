import bs4
import requests

html = requests.get('http://www.kultunaut.dk/perl/arrlist/type-nynaut?Area=&ArrStartday=22&ArrStartmonth=Marts&ArrStartyear=2020&ArrSlutday=29&ArrSlutmonth=Marts&ArrSlutyear=2020&ArrMaalgruppe=&DefaultGenre=Musik&ArrKunstner=')
txt = html.text
soup = bs4.BeautifulSoup(txt, 'html.parser')
events = soup.select('td h3 b')
print('number of events is {}'.format(len(events)))
for e in events:
    print(e.getText())