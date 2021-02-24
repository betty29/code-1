## Tailing a live log file with Python.  
Originally published: 2013-01-18 19:45:42  
Last updated: 2013-01-18 19:45:43  
Author: Gustavo Cordova  
  
I've seen several tail implementations and they've seemed overly complicated, or overengineered, for my purposes.

Here's an implementation I'm using in my production code, it's _ONLY_ for following an open stream, line by line, and sleeps for a second while waiting for activity. No heuristics, no configurability, it's simple and --in my opinion-- clean enough to understand in a single look.

Enjoy!!