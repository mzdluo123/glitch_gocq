import base64
import logging
import os
import subprocess
import sys
import threading
import time
from pathlib import Path

import requests

HEADERS = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67"}


def get_down_url():
    rsp = requests.get("https://api.github.com/repos/Mrs4s/go-cqhttp/releases/latest")
    rsp = rsp.json()
    print(f"Latest go-cqhttp version:{rsp['tag_name']}")
    for i in rsp["assets"]:
        if "linux_amd64.tar.gz" in i["name"]:
            return i["browser_download_url"]


def check_runnable():
    if not Path("./.data", "go-cqhttp").exists():
        down_url = get_down_url()
        content = requests.get(down_url, headers=HEADERS)
        with open(Path(".data", "download.tar.gz"), "wb")as file:
            file.write(content.content)
        os.system("cd ./.data/ && tar -zxvf ./download.tar.gz")

    os.chmod("./.data/go-cqhttp", 755)


def run_gocq():
    while True:
        process = subprocess.Popen("cd ./.data && ./go-cqhttp faststart", shell=True, stdin=sys.stdin,
                                   stdout=sys.stdout,
                                   stderr=sys.stderr)
        process.wait()
        time.sleep(10)


def keep_live(url: str):
    while True:
        try:
            requests.get(url, headers=HEADERS)
        except Exception as e:
            logging.exception(e)
        time.sleep(60)


def mv_config(env, file_name):
    if os.environ.get(env, None) is not None:
        file = Path(f"./.data/{file_name}")
        if file.exists():
            os.remove(file)
        with open(file, "w") as file:
            content = base64.b64decode(os.environ[env]).decode()
            file.write(content)


if __name__ == '__main__':
    if not Path(".data").exists():
        os.mkdir(".data")
    check_runnable()
    mv_config("CONF", "config.yml")
    mv_config("DEVICE", "devices.json")
    # os.system("refresh")  # 刷新glitch
    # os.system("git reset HEAD .")
    gocq_thread = threading.Thread(target=run_gocq)
    gocq_thread.isDaemon()
    gocq_thread.start()
    keep_live(os.environ["URL"])
