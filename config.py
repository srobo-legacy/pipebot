
HOST = "irc.freenode.net"
PORT = 6667
NICK = "srpipebot-dev"
IDENT = "srpipebot-dev"
REALNAME = "Student Robotics Pipebot"
CHANNEL = "#srobo"
LOG_PATH = '/home/pipebot/hash-srobo-log'
PIPE_PATH = "/tmp/hash-srobo"
MESSAGE_PREFIX = ""
VERBOSE = True

try:
    from localconfig import *
except ImportError:
    pass
