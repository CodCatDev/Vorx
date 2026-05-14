# ┌─────────────┐
# │ Vorx Engine │
# │─────────────│
# │ Console CLI │
# └─────────────┘

from sys import argv as rg

from .commands import cmdList

def main():
    argv = rg[1:]
    l = len(argv)
    if l == 0 or not argv[0] in commands.cmdList.keys():
        commands.cmdList['help']['function'](argv[:1])
    else:
        cmd = commands.cmdList[argv[0]]
        if cmd['function'] is not None:
            cmd['function'](argv[:1])
        else:
            print(f"Command not found")
            commands.cmdList['help']['function'](argv[:1])