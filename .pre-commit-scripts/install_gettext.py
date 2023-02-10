#!/usr/bin/env python3
import sys
import shlex
import shutil
import subprocess


def main():
    if sys.platform == "win32":
        try:
            cmd = shlex.split(
                "Set-ExecutionPolicy RemoteSigned -Scope CurrentUser;irm get.scoop.sh | iex;scoop install gettext", posix=False
            )
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
        cmd = shlex.split("sudo apt --update && sudo apt install -y gettext", posix=True)
    else:  # macOS
        cmd = shlex.split("brew update && brew install gettext", posix=True)
    return subprocess.run(cmd, shell=False, check=True)


if __name__ == "__main__":
    exit(main())
