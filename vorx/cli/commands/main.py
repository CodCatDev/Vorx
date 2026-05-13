from ...conf import VERSION, BUILD, BUILD_DATE, SERVER_SOCK
from platform import system, python_version, architecture, python_implementation, release
from ..commands import list as l
from threading import Thread
from time import time
from os import makedirs, getcwd, path, getlogin
from http.client import HTTPSConnection
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
            conn = HTTPSConnection(SERVER_SOCK, 443, timeout=5)
            conn.request("HEAD", "/")
            self.res = conn.getresponse()
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

def help(args: list):
    verInfo = f"Version {VERSION}-{BUILD}"
    sysInfo = f"Run on {system()} {release()} with {python_implementation()} {python_version()}"
    pad1 = round(len(logo.splitlines()[0]) / 2 - len(verInfo) / 2)
    pad2 = round(len(logo.splitlines()[0]) / 2 - len(sysInfo) / 2)
    cmds = ""
    for cmd in l.list.keys():
        pad = 10 - len(cmd)
        cmds += f"\n    {cmd}{' ' * pad}{l.list[cmd]['description']}"
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
        print(f"\rPing done! {t.ping:.2f} ms, status: {t.res.status} {t.res.reason}")
        if t.res.status != 200:
            print(f"{c.yellow}Warning: Server is responding but returned an error status code! This may indicate a problem with the server. Please check the server status or try again later.{c.reset}")
    
def init(args: list):
    print(logo)
    print("Adding a basic configuration...")
    currDir = getcwd()

    name = input("Project name: ")
    if len(name) == 0:
        print(f"{c.yellow}Warn! Project name cannot be empty! Setting it to default..{c.reset}")
        name = "MyVorxProject"
    author = input("Author name: ")
    if len(author) == 0:
        print(f"{c.red}Error! Author name cannot be empty! Setting it to pc username..{c.reset}")
        author = getlogin()

    makedirs(path.join(currDir, ".vorx"), exist_ok=True)
    makedirs(path.join(currDir, "assets"), exist_ok=True)
    makedirs(path.join(currDir, "scripts"), exist_ok=True)
    makedirs(path.join(currDir, "scenes"), exist_ok=True)
    with open(path.join(currDir, ".vorx", "config.json"), "w", encoding="utf-8") as f:
        data ={
            "name": name,
            "author": author,
            "gameVersion": "1.0.0",
            "engineVersion": f"{VERSION}-{BUILD}",
            "serverSync": True
        }
        dump(data, f, indent=4, sort_keys=True, ensure_ascii=False)
    with open(path.join(currDir, "README.md"), "w", encoding="utf-8") as f:
        readme = f"""<div align="center">
    <h1> 🚀 {name}</h1>

![Engine](https://img.shields.io/badge/Engine-Vorx_2026.0.2-orange?style=flat-square)
![Build](https://img.shields.io/badge/Build-dev-blue?style=flat-square)
</div>


## 👤 by: {author}

## 🛠 Run:

install [VorxEngine](https://github.com/CodCatDev/Vorx)

import project to Vorx Engine

and run from Vorx editor"""
        f.write(readme)
    print(f"{c.green}Configuration added!{c.reset}")