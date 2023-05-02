import argparse
import collections
import contextlib
import glob
import os
from pprint import pprint

import polib

parser = argparse.ArgumentParser()
parser.add_argument(
    "path",
    nargs="?",
    default=None,
    help="Path to the .po file or directory containing .po files",
)
parser.add_argument("-t", "--threshold", type=int, default=85)
args = parser.parse_args()

subject = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
    )
)

is_file = False

with contextlib.suppress(TypeError):
    if os.path.isdir(args.subject):
        is_file = False
        subject = os.path.abspath(args.subject)

    elif os.path.isfile(args.subject):
        is_file = True
        subject = (
            args.subject
            if os.path.isabs(args.subject)
            else os.path.join(subject, args.subject)
        )

    else:
        print("Invalid subject, showing all files.")

DELIMITERS = ("``", "*")


def has_delimiters(x):
    return any(d in x for d in DELIMITERS)


def main(subject):
    subject = [subject] if is_file else glob.glob(f"{subject}**/**/*.po")
    files_with_differences = collections.defaultdict(list)

    for _, pofilename in enumerate(subject):
        po = polib.pofile(pofilename)
        if po.percent_translated() < min(args.threshold, 100):
            continue

        for entry in po:
            wordsid = wordsstr = []

            if has_delimiters(entry.msgid):
                wordsid = [word for word in entry.msgid.split() if has_delimiters(word)]

            if has_delimiters(entry.msgstr):
                wordsstr = [
                    word for word in entry.msgstr.split() if has_delimiters(word)
                ]

            if len(wordsid) != len(wordsstr):
                key = pofilename
                files_with_differences[key].append(
                    {
                        "occurrences": entry.occurrences,
                        "words": {
                            "original": wordsid,
                            "translated": wordsstr,
                        },
                    }
                )

    return files_with_differences


if __name__ == "__main__":
    pprint(main(subject))
