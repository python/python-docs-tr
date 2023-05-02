import os
from argparse import ArgumentParser
from functools import lru_cache
from subprocess import check_output

import polib

parser = ArgumentParser()
parser.add_argument(
    "path",
    nargs="?",
    default=None,
    help="Path to the .po file or directory containing .po files",
)
parser.add_argument(
    "--no-cache", action="store_true", default=False, help="Don't use cache"
)
args = parser.parse_args()


def main():
    global git_root
    total_progress = False
    git_root = get_git_root()

    if args.no_cache:
        progress.cache_clear()
        get_git_root.cache_clear()

    if args.path is None:
        print("No path specified, showing total progress...")
        args.path = os.path.abspath(git_root).replace("\\", "/")
        total_progress = True

    else:
        args.path = os.path.abspath(args.path).replace("\\", "/")

    if os.path.isfile(args.path):
        paths = [args.path]

    elif os.path.isdir(args.path):
        paths = []
        for root, _, files in os.walk(args.path):
            paths.extend(
                os.path.join(root, file) for file in files if file.endswith(".po")
            )
        paths = map(lambda x: x.replace("\\", "/"), paths)

    else:
        print("Invalid path")
        return -1

    try:
        progress(tuple(paths), total_progress)
        return 0
    except Exception as e:
        print(f"Error: {e}")
        return -1


@lru_cache(maxsize=512)
def progress(paths, total_progress=False):
    total = 0
    translated = 0
    previous = "/"
    is_root = True
    for path in paths:
        pofile = polib.pofile(path)
        total += len(pofile) - len(pofile.obsolete_entries())
        translated += len(pofile.translated_entries())
        path = path.replace(f"{git_root}", "")
        if is_root and len(path.split("/")) == 2:
            print()
            print("PYTHON-DOCS-TR")
            print("-" * 14)
            is_root = False
        if (previous.split("/")[1] != path.split("/")[1]) and len(path.split("/")) > 2:
            print()
            print(path.split("/")[1].upper())
            print("-" * len(path.split("/")[1].upper()))
        previous = path
        print(f"{path}: {pofile.percent_translated()}%")

    dir_path = args.path.replace(f"{git_root}", "/").replace("//", "/")
    total_progress_of = "/" if total_progress else dir_path
    print()
    print(
        f"Total progress of {total_progress_of}: {round(translated / total * 100, 2)}%"
    ) if len(paths) > 1 else None


@lru_cache(maxsize=1)
def get_git_root():
    return os.path.abspath(
        check_output(["git", "rev-parse", "--show-toplevel"]).decode("utf-8").strip()
    ).replace("\\", "/")


if __name__ == "__main__":
    main()
