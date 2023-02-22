#!/usr/bin/env python3
import sys
import shutil
import shlex
import subprocess


def main():
    if sys.platform == "win32":
        powershell = shutil.which("powershell.exe")
        install = subprocess.run(
            shlex.split("pip install git+https://github.com/egeakman/powrap.git@v1.0.2", posix=False), shell=True, executable=powershell
        )
        run = subprocess.run(shlex.split(f"powrap {sys.argv[1]} --quiet", posix=False), shell=True, executable=powershell)

    else:
        install = subprocess.run(shlex.split("pip install git+https://github.com/egeakman/powrap.git@v1.0.2", posix=True))
        run = subprocess.run(shlex.split(f"powrap {sys.argv[1]} --quiet", posix=True))

    return any([install.returncode, run.returncode])


if __name__ == "__main__":
    exit(main())
