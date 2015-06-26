#!/usr/bin/env python3

from argparse import ArgumentParser
import dublinbus


def parse_args():
    ap = ArgumentParser()
    ap.add_argument('stop_number', type=int)
    return ap.parse_args()


def main():
    args = parse_args()
    print(dublinbus.print_stop(args.stop_number))


if __name__ == '__main__':
    main()
