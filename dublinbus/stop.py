# monitor.py
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
from tabulate import tabulate

BASEURL = 'http://rtpi.ie/Text/WebDisplay.aspx?stopRef='


def print_stop(stop_number):
    if isinstance(stop_number, int):
        stop_number = str(stop_number)

    stop_number = stop_number.zfill(5)
    current_url = "%s%s" % (BASEURL, stop_number)
    data = urllib.request.urlopen(current_url).read()
    soup = BeautifulSoup(str(data))
    buses = []
    for row in soup.find('table').findAll('tr'):
        entries = row.findAll('td')
        if entries:
            buses.append([e.contents[0] for e in entries])

    return(tabulate(buses,
                    headers=['service', 'direction', 'time', 'low floor']))
