
import os

try:
    from localconfig import PIPE_PATH
except ImportError:
    PIPE_PATH = "/tmp/hash-srobo"

def open_fifo():
    fifofd = os.open( PIPE_PATH, os.O_WRONLY | os.O_NONBLOCK )
    return fifofd

def say(message):
    if not message.endswith('\n'):
        message += '\n'
    fd = open_fifo()
    with os.fdopen(fd, 'a') as fifo:
        fifo.write(message)
