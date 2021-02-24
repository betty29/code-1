## Log watcher (tail -F *.log)  
Originally published: 2011-11-29 18:31:01  
Last updated: 2014-04-04 15:54:03  
Author: Giampaolo Rodolà  
  
A python class which "watches" a directory and calls a callback(filename, lines) function every time one of the files being watched gets written, in real time.

Practically speaking, this can be compared to *"tail -F *.log"* UNIX command, but instead of having lines printed to stdout a python function gets called.

Similarly to tail, it takes care of "watching" new files which are created after initialization and "unwatching" those ones which are removed in the meantime. This means you'll be able to "follow" and support also rotating log files.

**History**

- rev5 (2013-04-05): 
  - sizehint parameter
- rev4 (2013-03-16): 
  - python 3 support (also dropped support for python <= 2.5)
  - windows support
  - unit tests
  - main class can also be used as a context manager
- rev3 (2012-01-13): initial release