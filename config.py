
HOST = "irc.freenode.net"
PORT = 6667
NICK = "srpipebot-dev"
IDENT = "srpipebot-dev"
REALNAME = "Student Robotics Pipebot"
CHANNEL = "#srobo-bots"
PIPE_PATH = "/tmp/hash-srobo"
MESSAGE_PREFIX = "srbot: say #srobo "
VERBOSE = True

try:
    from localconfig import *
except ImportError:
    pass
