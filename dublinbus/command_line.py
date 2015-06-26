#!/usr/bin/env python3

from argparse import ArgumentParser
from subprocess import check_output
from tabulate import tabulate
from time import sleep
import dublinbus


def notify(msg):
    check_output(['notify-send', msg])


def split_commas(s):
    return s.split(',')


def int_range(s):
    return [int(t) for t in s.split(':')]


def parse_args():
    ap = ArgumentParser()
    ap.add_argument('stop_number', type=int, help="Stop number")
    ap.add_argument('bus_numbers', nargs='?', type=split_commas,
                    help="Bus numbers, comma separated")
    ap.add_argument('-n', '--notify', type=int_range,
                    help="Notify incoming bus within a time range min:max")
    return ap.parse_args()


def print_tabulate(buses):
    print(tabulate(buses,
          headers=['service', 'direction', 'time', 'low floor']))


def main():
    args = parse_args()

    if not args.notify:
        buses = dublinbus.print_stop(
            args.stop_number,
            bus_numbers=args.bus_numbers
        )
        print_tabulate(buses)
        return

    while True:
        buses = dublinbus.print_stop(
            args.stop_number,
            bus_numbers=args.bus_numbers
        )
        print_tabulate(buses)
        if not buses:
            notify("No buses available :(")
            sleep(60 * 5)
            continue

        bn = buses[0][0]
        eta = buses[0][2]
        if eta.endswith(' Mins'):
            eta = int(eta[:-5])

        elif eta == 'Due':
            eta = 0

        else:
            print("Unable to parse %r" % eta)
            return

        if eta == args.notify[0]:
            notify("** %s due in %d minutes, hurry! **" % (bn, eta))

        elif args.notify[0] < eta <= args.notify[1]:
            notify("%s due in %d minutes" % (bn, eta))

        sleep(60)


if __name__ == '__main__':
    main()
