import os
import argparse
import contextlib
import glob
import polib


parser = argparse.ArgumentParser()
parser.add_argument("subject", nargs="?", default=None, help="Subject to check (file or directory)")
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
        args.org_subject = args.subject
        args.subject = args.subject if os.path.isabs(args.subject) else os.path.join(PO_DIR, args.subject)

    else:
        print("Invalid subject, showing all files.")


def po_stats(pofilename):
    po = polib.pofile(pofilename)
    translated = len(po.translated_entries())
    total = len(po) + translated
    return (po.percent_translated(), translated, total)


def main():
    files = []
    translated = []
    total = []
    if is_file:
        po = polib.pofile(args.subject)
        return os.path.relpath(args.org_subject), po.percent_translated()

    for pofilename in glob.glob(f"{PO_DIR}**/*.po"):
        stats = po_stats(pofilename)
        translated.append(stats[1])
        total.append(stats[2])
        files.append((os.path.relpath(pofilename).replace("\\", "/"), stats[0]))
    for pofilename in glob.glob(f"{PO_DIR}**/**/*.po"):
        stats = po_stats(pofilename)
        translated.append(stats[1])
        total.append(stats[2])
        files.append((os.path.relpath(pofilename).replace("\\", "/"), stats[0]))
    return files, round(sum(translated) / sum(total) * 100, 1)


if __name__ == "__main__":
    files, weighted_progress = main()
    if not args.subject:
        print("No subject provided, showing general progress")
        print(f"{len([file for file in files if file[1] > min(args.threshold, 100)])} / {len(files)} files completed")
        print(f"Weighted progress: {weighted_progress}%\n")

        if args.completed:
            print("Completed files:")
            completed_files = [file for file in files if file[1] > min(args.threshold, 100)]
            for file, percentage in completed_files:
                print(f"{file}: {percentage}%")
    elif is_file:
        print(f"{files}: {weighted_progress}%")

    else:
        print(f"{len([file for file in files if file[1] > min(args.threshold, 100)])} / {len(files)} files completed")
        print(f"Weighted progress: {weighted_progress}%\n")

        if args.completed:
            print('Completed files:')
            completed_files = [file for file in files if file[1] > min(args.threshold, 100)]
            for file, percentage in completed_files:
                print(f"{file}: {percentage}%")
