#!/usr/bin/env python3
import sys
import shutil
import subprocess


def main():
    if sys.platform == "win32":
        try:
            cmd = "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser;irm get.scoop.sh | iex;scoop install gettext"
            print("test")
            return subprocess.run(cmd, shell=True, check=True, executable=shutil.which("powershell"))
        except Exception:
            print(
                NotImplementedError(
                    "WARNING: Use scoop to install gettext on Windows!!! Otherwise powrap will fail.\nRefer to \
https://github.com/python/python-docs-tr/blob/HEAD/wiki/gettext.md for instructions."
                )
            )
            exit(0)
    elif sys.platform in ["linux", "linux2"]:
        print("test2")
        cmd = "sudo apt --upgrade && sudo apt install -y gettext"
    else:  # macOS
        print("test3")
        cmd = "brew update && brew install gettext"
    return subprocess.run(cmd, shell=True, check=True)


if __name__ == "__main__":
    exit(main())
