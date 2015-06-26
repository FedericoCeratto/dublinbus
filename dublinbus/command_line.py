#!/usr/bin/env python3

from argparse import ArgumentParser
import dublinbus


def parse_args():
    ap = ArgumentParser()
    ap.add_argument('stop_number', type=int, help="Stop number")
    ap.add_argument('bus_numbers', nargs='?',
                    help="Bus numbers, comma separated")
    return ap.parse_args()


def main():
    args = parse_args()
    if args.bus_numbers:
        bn = args.bus_numbers.split(',')
        print(dublinbus.print_stop(args.stop_number,
                                   bus_numbers=bn))

    else:
        print(dublinbus.print_stop(args.stop_number))


if __name__ == '__main__':
    main()
