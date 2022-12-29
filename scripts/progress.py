import os
import argparse
import contextlib
import glob
import polib


parser = argparse.ArgumentParser()
parser.add_argument(
    "subject", nargs="?", default=None, help="Subject to check (file or directory)"
)
parser.add_argument("-c", "--completed", action="store_true")
parser.add_argument("-t", "--threshold", type=int, default=90)
args = parser.parse_args()

PO_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
    )
)

is_file = False

with contextlib.suppress(TypeError):
    if os.path.isdir(args.subject):
        PO_DIR = os.path.abspath(args.subject)

    elif os.path.isfile(args.subject):
        is_file = True
        args.subject = (
            args.subject
            if os.path.isabs(args.subject)
            else os.path.join(PO_DIR, args.subject)
        )

    else:
        print("Invalid subject, showing all files.")


def main():
    files = []
    if is_file:
        po = polib.pofile(args.subject)
        return [[args.subject.replace(PO_DIR, ""), po.percent_translated()]]

    for pofilename in glob.glob(f"{PO_DIR}**/*.po"):
        po = polib.pofile(pofilename)
        files.append((pofilename.replace(PO_DIR, ""), po.percent_translated()))
    for pofilename in glob.glob(f"{PO_DIR}**/**/*.po"):
        po = polib.pofile(pofilename)
        files.append((pofilename.replace(PO_DIR, ""), po.percent_translated()))
    return files


if __name__ == "__main__":
    results = [f"{file[0]}: {file[1]}%" for file in main()]

    for result in results:
        if args.completed and int(result.split(" ")[1].replace("%", "")) > min(
            args.threshold, 100
        ):
            print(result)
        elif not args.completed:
            print(result)
