
HOST = "irc.freenode.net"
PORT = 6667
NICK = "srpipebot-dev"
IDENT = "srpipebot-dev"
REALNAME = "Student Robotics Pipebot"
CHANNEL = "#srobo"
PIPE_PATH = "/var/run/hash-srobo"
MESSAGE_PREFIX = ""
VERBOSE = True

try:
    from localconfig import *
except ImportError:
    pass
