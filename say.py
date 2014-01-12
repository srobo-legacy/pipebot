
import os

PIPE_PATH="/tmp/hash-srobo"

def open_fifo():
    fifofd = os.open( PIPE_PATH, os.O_WRONLY | os.O_NONBLOCK )
    return fifofd

def say(message):
    fd = open_fifo()
    with os.fdopen(fd, 'a') as fifo:
        fifo.write(message)
