#!/usr/bin/env python3
import os
import sys
import shlex
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
            subprocess.run(shlex.split(f"mkdir -p {gettext_path}", posix=False), shell=True, executable=powershell)
            
            response = requests.get(gettext_url)
            with open(gettext_zip, "wb") as f:
                f.write(response.content)
            
            with ZipFile(gettext_zip, "r") as zip:
                zip.extractall(gettext_path)
                
            os.remove(gettext_zip)
            os.environ["PATH"] += os.pathsep + os.path.join(gettext_path, "bin")

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
