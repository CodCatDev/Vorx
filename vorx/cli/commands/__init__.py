from . import main
from .cmdList import cmdList

cmdList['help']['function'] = main.cmdHelp
cmdList['version']['function'] = main.version
cmdList['ping']['function'] = main.ping
cmdList['init']['function'] = main.init