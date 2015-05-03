Pipebot is a utility for sending arbitrary messages to an IRC channel from a FIFO on a server.

## Usage

From the command line:
~~~~
$ ./say "I'm a puppet on a string"
~~~~

Things are a little more complicated to use Pipebot from software.
Because Pipebot accepts messages via a fifo, this will block if Pipebot isn't running.
Where possible, messages should therefore be transmitted into the fifo using a non-block flag,
 however this is not supported in some languages (eg: PHP).

In order to support messages from languages Pipebot from deficient languages,
 the CLI script that can be used as a wrapper to the FIFO plus language
 native wrappers that make use of this.
It is expected that this repo will be included as a submodule of any project
 that would like Pipebot integration, and the supplied wrappers used,
 rather than going direct to the FIFO.

## Configuration

Various aspects of the bot can be configured by introducing a `localconfig.py`
 file next to the `config.py` file.

**Note**: the default config is aimed at deployment so developers will probably
 want to override many of the values, almost certainly including `PIPE_PATH`
 and `CHANNEL`.
