# monitor.py
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from tabulate import tabulate

url = 'http://rtpi.ie/Text/WebDisplay.aspx?stopRef='


def print_stop(stop_number):
    current_url = url + stop_number
    data = urllib.request.urlopen(current_url).read()
    soup = BeautifulSoup(str(data))
    buses = []
    for row in soup.find('table').findAll('tr'):
        entries = row.findAll('td')
        if entries:
            buses.append(list(map((lambda x: x.contents[0]), entries)))
    return(tabulate(buses,
                    headers=['service', 'direction', 'time', 'low floor']))
