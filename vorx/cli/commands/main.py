from ...conf import VERSION, BUILD, BUILD_DATE, SERVER_SOCK
from platform import system, python_version, architecture, python_implementation, release
from ..commands import list as l
from threading import Thread
from time import time
from socket import socket

class PingThread(Thread):
    def __init__(self):
        super().__init__()
        self.daemon = True
        self.response = None
        self.startTime = 0.0
        self.endTime = 0.0
        self.ping = 0.0
        self.error = None

    def run(self):
        try:
            self.startTime = time()
            with socket() as s:
                s.settimeout(5)
                s.connect((SERVER_SOCK, 80))
            self.endTime = time()
            self.ping = (self.endTime - self.startTime) * 1000
        except Exception as e:
            self.error = str(e)
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
        print(f"\rError pinging server:\nResponsed in {t.ping:.2f} ms\nError: {t.error}")
    else:
        print(f"\rPing done! {t.ping:.2f} ms") 