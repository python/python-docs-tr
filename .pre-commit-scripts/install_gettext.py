#!/usr/bin/env python3
import os
import sys
import shutil
import requests
import subprocess
from zipfile import ZipFile


def main():
    if sys.platform == "win32":
        powershell = shutil.which("powershell.exe")
        gettext_url = "https://github.com/vslavik/gettext-tools-windows/releases/download/v0.21.1/gettext-tools-windows-0.21.1.zip"
        gettext_path = os.path.join(os.environ["LOCALAPPDATA"], "Programs", "gettext-tools")
        gettext_zip = os.path.join(gettext_path, "gettext-tools.zip")

        try:
            None if os.path.exists(gettext_path) else os.mkdir(gettext_path)

            if not os.path.exists(os.path.join(gettext_path, "bin")):
                response = requests.get(gettext_url)
                with open(gettext_zip, "wb") as f:
                    f.write(response.content)

                with ZipFile(gettext_zip, "r") as zip:
                    zip.extractall(gettext_path)

            os.remove(gettext_zip) if os.path.exists(gettext_zip) else None

            p = subprocess.run("$profile.CurrentUserCurrentHost", shell=True, executable=powershell, capture_output=True, text=True)
            with open(p.stdout.strip("\n"), "a+") as f:
                command = f"$Env:PATH += '{os.pathsep + os.path.join(gettext_path, 'bin')}'"
                f.seek(0)
                if command not in f.readlines():
                    print("Adding gettext to PATH...")
                    f.write(f"\n{command}")
                else:
                    print("gettext is already in PATH")

        except Exception as e:
            print(e)
            return 1

        else:
            return 0

    elif sys.platform in ["linux", "linux2"]:
        cmd = "sudo apt update; sudo apt install -y gettext"
    else:  # macOS
        cmd = "brew update; brew install gettext"
    return subprocess.run(cmd, shell=True).returncode


if __name__ == "__main__":
    print("Installing gettext...")
    exit(main())
