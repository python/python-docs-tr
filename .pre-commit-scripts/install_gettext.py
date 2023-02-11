#!/usr/bin/env python3
import sys
import shlex
import shutil
import subprocess


def main():
    if sys.platform == "win32":
        executable = shutil.which("powershell.exe")
        cmd = shlex.split("Set-ExecutionPolicy RemoteSigned -Scope CurrentUser;irm get.scoop.sh | iex", posix=False)
        p_scoop = subprocess.run(cmd, shell=True, executable=executable)
        p_install = subprocess.run(shlex.split("scoop install gettext", posix=False), shell=True, executable=executable)

        return p_scoop.returncode or p_install.returncode

    elif sys.platform in ["linux", "linux2"]:
        cmd = "sudo apt update; sudo apt install -y gettext"
    else:  # macOS
        cmd = "brew update; brew install gettext"
    return subprocess.run(cmd, shell=True).returncode


if __name__ == "__main__":
    exit(main())
