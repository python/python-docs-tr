#!/usr/bin/env python3

import os
import argparse
import regex
import polib
from glob import glob
from tabulate import tabulate
from textwrap import fill


def find_in_po(pattern):
    table = []
    try:
        _, columns = os.popen("stty size", "r").read().split()
        available_width = int(columns) // 2 - 3
    except Exception:
        available_width = 80 // 2 - 3

    for file in glob("**/*.po"):
        pofile = polib.pofile(file)
        table.extend(
            [
                fill(entry.msgid, width=available_width),
                fill(entry.msgstr, width=available_width),
            ]
            for entry in pofile
            if entry.msgstr and regex.search(pattern, entry.msgid)
        )

    print(tabulate(table, tablefmt="fancy_grid"))


def parse_args():
    parser = argparse.ArgumentParser(description="Find translated words.")
    parser.add_argument("pattern")
    return parser.parse_args()


def main():
    args = parse_args()
    find_in_po(args.pattern)


if __name__ == "__main__":
    main()
