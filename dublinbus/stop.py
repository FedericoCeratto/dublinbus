# monitor.py
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

BASEURL = 'http://rtpi.ie/Text/WebDisplay.aspx?stopRef='


def print_stop(stop_number, bus_numbers=None):
    if isinstance(stop_number, int):
        stop_number = str(stop_number)

    stop_number = stop_number.zfill(5)
    current_url = "%s%s" % (BASEURL, stop_number)
    data = urllib.request.urlopen(current_url).read()
    soup = BeautifulSoup(str(data))
    buses = []
    for row in soup.find('table').findAll('tr'):
        entries = row.findAll('td')
        if not entries:
            continue

        bn = entries[0].contents[0]
        if bus_numbers is None or bn in bus_numbers:
            buses.append([e.contents[0] for e in entries])

    return buses
