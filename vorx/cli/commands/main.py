from ...conf import VERSION, BUILD, BUILD_DATE, PING_SOCK
from platform import system, python_version, architecture, python_implementation, release
from ..commands.cmdList import cmdList as l
from threading import Thread
from time import time
from os import makedirs, getcwd, getlogin
from pathlib import Path
from requests import get
from json import dump

class c:
    cyan = "\033[96m"
    green = "\033[92m"
    yellow = "\033[93m"
    red = "\033[91m"
    reset = "\033[0m"

class PingThread(Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.res = None
        self.startTime = 0.0
        self.endTime = 0.0
        self.ping = 0.0
        self.error = None

    def run(self):
        try:
            self.startTime = time()
            conn = get(PING_SOCK)
            self.res = conn
            conn.close()
            self.endTime = time()
        except Exception as e:
            self.error = str(e)
            self.res = None
            self.endTime = time()
        self.ping = (self.endTime - self.startTime) * 1000


logo = """ _    __                ______            _         
| |  / /___  ______  __/ ____/___  ____ _(_)___  ___ 
| | / / __ \\/ ___/ |/_/ __/ / __ \\/ __ `/ / __ \\/ _ \\
| |/ / /_/ / /  _>  </ /___/ / / / /_/ / / / / /  __/
|___/\\____/_/  /_/|_/_____/_/ /_/\\__, /_/_/ /_/\\___/ 
                                /____/               """

def cmdHelp(args: list):
    verInfo = f"Version {VERSION}-{BUILD}"
    sysInfo = f"Run on {system()} {release()} with {python_implementation()} {python_version()}"
    pad1 = round(len(logo.splitlines()[0]) / 2 - len(verInfo) / 2)
    pad2 = round(len(logo.splitlines()[0]) / 2 - len(sysInfo) / 2)
    cmds = ""
    for cmd in l.keys():
        pad = 10 - len(cmd)
        cmds += f"\n    {cmd}{' ' * pad}{l[cmd]['description']}"
    text = f"""{logo}
{' ' * pad1}{verInfo}
{' ' * pad2}{sysInfo}

usage: vorx [command] [options]

Commands:{cmds}"""
    print(text)

def version(args: list):
    print(logo)
    print(f"Vorx Engine version {VERSION}-{BUILD}")
    print(f"Build type: {'Development' if BUILD == 'dev' else 'Release'}, build date: {BUILD_DATE}")
    print(f"Running on {system()} {release()} ({architecture()[1]} {architecture()[0]}) with {python_implementation()} {python_version()}")
    print(f"Copyright (c) 2026 CodCatDev. All rights reserved.")
    print("Licensed under Apache License, Version 2.0")

def ping(args: list):
    print(logo)
    print("Pinging a Vorx server...")

    t = PingThread()
    t.start()
    anim = ["|", "/", "-", "\\"]
    while t.is_alive():
        print(f"\r{anim[0]}", end="", flush=True)
        anim = anim[1:] + [anim[0]]
        t.join(0.1)
    if t.error is not None:
        print(f"\r{c.red}Error pinging server:\nResponded in {t.ping:.2f} ms\nError: {t.error}{c.reset}")
    else:
        print(f"\rPing done! {t.ping:.2f} ms, status: {t.res.status_code}")
        try:
            js = t.res.json()
        except:
            print(f"{c.red}Error parsing server response! Maybe the server is down?{c.reset}")
            print(f"Response: {t.res.text}")
            exit(1)
        print(f"Server status:")
        print(f"  - Uptime: {js.get('data').get('uptimeText')}")
        print(f"  - Memory: {js.get('data').get('ramPercent')}%")
        print(f"  - CPU: {js.get('data').get('cpuPercent')}%")
        print(f"  - Api Version: v{js.get('apiVersion')}")
        if t.res.status_code != 200:
            print(f"{c.yellow}Warning: Server is responding but returned an error status code! This may indicate a problem with the server. Please check the server status or try again later.{c.reset}")
    
def init(args: list):
    print(logo)
    print("Adding a basic configuration...")
    currDir = Path(getcwd()).resolve()

    name = input("Project name: ")
    if len(name) == 0:
        print(f"{c.yellow}Warn! Project name cannot be empty! Setting it to default..{c.reset}")
        name = "MyVorxProject"
    author = input("Author name: ")
    if len(author) == 0:
        print(f"{c.red}Error! Author name cannot be empty! Setting it to pc username..{c.reset}")
        author = getlogin()

    makedirs(currDir / name, exist_ok=True)
    currDir = Path(currDir / name).resolve()

    makedirs(currDir / ".vorx", exist_ok=True)
    makedirs(currDir / "scenes", exist_ok=True)
    makedirs(currDir / "scripts", exist_ok=True)
    makedirs(currDir / "assets", exist_ok=True)
    with open(currDir / ".vorx" / "config.json", "w", encoding="utf-8") as f:
        data ={
            "name": name,
            "author": author,
            "gameVersion": "1.0.0",
            "engineVersion": f"{VERSION}-{BUILD}",
            "serverSync": True,
            "defaultScene": "start",
            "data": {
                "scenes":{
                    "start": "defaultScene"
                }
            }
        }
        dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)
    with open(currDir /"README.md", "w", encoding="utf-8") as f:
        readme = f"""<div align="center">
    <h1> 🚀 {name}</h1>

![Engine](https://img.shields.io/badge/Engine-Vorx_{VERSION}-orange?style=flat-square)
![Build](https://img.shields.io/badge/Build-{BUILD}-blue?style=flat-square)
</div>


## 👤 by: {author}

## 🛠 Run:

install [VorxEngine](https://github.com/CodCatDev/Vorx)

import project to Vorx Engine

and run from Vorx editor"""
        f.write(readme)
    myDir = Path(__file__).resolve().parent
    with open(myDir / "_scriptMain.py", "r", encoding="utf-8") as f:
        main = f.read()
    with open(currDir / "vorxMain.py", "w", encoding="utf-8") as f:
        f.write(main)
    
    with open(myDir / "_sceneMain.vxs", "r", encoding="utf-8") as f:
        sceneMain = f.read()
    with open(currDir / "scenes" / "defaultScene.vxs", "w", encoding="utf-8") as f:
        f.write(sceneMain)
    print(f"{c.green}Configuration added!{c.reset}")