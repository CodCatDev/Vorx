# ┌─────────────┐
# │ Vorx Engine │
# │─────────────│
# │ Console CLI │
# └─────────────┘

# Imports
from platform import system, architecture, python_version, python_implementation
from sys import argv as rg
from requests import get
from threading import Thread
from time import time

class PingThread(Thread):
    def __init__(self):
        super().__init__(daemon=True)
        self.response = None
        self.error = None
        self.endTime = 0.0

    def run(self):
        try:
            self.response = get("https://vorx.codcatdev.site", stream=True, timeout=10)
            self.endTime = time()
        except Exception as e:
            self.error = e

# Logo
logo = """ _    __                ______            _          
| |  / /___  ______  __/ ____/___  ____ _(_)___  ___ 
| | / / __ \\/ ___/ |/_/ __/ / __ \\/ __ `/ / __ \\/ _ \\
| |/ / /_/ / /  _>  </ /___/ / / / /_/ / / / / /  __/
|___/\\____/_/  /_/|_/_____/_/ /_/\\__, /_/_/ /_/\\___/ 
                                /____/               """

def main():
    CliClient('26.0.1', 'dev')

# CLI
class CliClient:
    def __init__(self, ver="UNK", build="UNK"):
        self.ver = ver
        self.build = build
        # Data
        self.sys = system()
        self.arc = architecture()[0]
        self.pyv = python_version()
        self.pyi = python_implementation()
        self.cliStartArgs = ["help", "ping"]
        # Args

        argv = rg[:]

        argv.pop(0)
        l = len(argv)
        if l == 0 or not argv[0] in self.cliStartArgs or argv[0] == "help":
            self._help()
        elif argv[0] == "ping":
            self._ping()
    
    def _help(self):
        verText = f"Version: {self.ver}-{self.build}"
        pad1 = " "*(round(len(logo.splitlines()[0])/2) - round(len(verText)/2))
        text = f"""{logo}
{pad1} {verText}
VorxEngine CLI, Running on {self.sys} {self.arc}, {self.pyi} {self.pyv}

Usage: vorx [command]

Commands:
    help       Show this help message
    ping       Pings the VORX-INFO server"""
        print(text)
    
    def _ping(self):

        try:
            print("Pinging a main server... (vorx.codcatdev.site)")
        
            g = PingThread()
            startTime = time()
            g.start()

            anim = "|/-\\"
            animI = 0

            while g.is_alive():
                g.join(0.5)
                print(f"\r{anim[animI]}", end="", flush=True)
                animI += 1
                if animI == 4:
                    animI = 0
            
            pingTime = (g.endTime - startTime) * 1000

            if g.response is not None:
                print(f"\rPing successful! TTFB - {pingTime:.2f}ms")
            else:
                print(f"\rPing failed. Check your internet connection.")
                exit(1)
        except Exception as e:
            print(f"\rError: {e}")
