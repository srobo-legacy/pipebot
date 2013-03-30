
HOST = "irc.freenode.net"
PORT = 6667
NICK = "srpipebot-dev"
IDENT = "srpipebot-dev"
REALNAME = "Student Robotics Pipebot"
CHANNEL = "#srobo-bots"
PIPE_PATH = "/tmp/hash-srobo"
TARGET_BOT = "srbot"
VERBOSE = True

try:
    from localconfig import *
except ImportError:
    pass
