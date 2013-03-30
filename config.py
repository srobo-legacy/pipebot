
HOST="irc.freenode.net"
PORT=6667
NICK="srpipebot-dev"
IDENT="srpipebot-dev"
REALNAME="srpipebot-dev"
CHANNEL="#srobo-bots"
PIPE_PATH="/tmp/hash-srobo"
TARGET_BOT="srbot"

try:
    from localconfig import *
except ImportError:
    pass
