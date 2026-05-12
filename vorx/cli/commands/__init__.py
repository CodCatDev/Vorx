from . import main
from . import list

list.list['help']['function'] = main.help
list.list['version']['function'] = main.version
list.list['ping']['function'] = main.ping
list.list['init']['function'] = main.init