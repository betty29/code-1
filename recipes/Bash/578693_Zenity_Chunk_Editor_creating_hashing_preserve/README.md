## Zenity Chunk Editor, creating an hashing to preserve Code Integrity.  
Originally published: 2013-10-22 01:30:41  
Last updated: 2013-10-22 01:30:42  
Author: Patrick Riendeau  
  
It Open by default a uuid-like temporary file. There is no actual was to modify the name, but assuming the implementation of ZenityShellEval imply a limited acces to shell, you might recuperate information from shell or futur adding to transfer a name or simple renaming the uuid-like file-name... This is to prevent auto-execution of a script from canned-design by playing with without having all clearly create your shell script and/or having fully pseudo-code explained and having confirmation of your design work...

Initially, the shell Editor look like this : is: ![Image of Zenity Shell In action](https://github.com/priendeau/Fnct.d#ZenityShellEval)

The dependency are simple, it require My GitHub Fnct.D project, available here: `[link](https://github.com/priendeau/Fnct.d)` to be installed inside /etc/init.d/Fnct.D like this 

git clone https://github.com/priendeau/Fnct.d /etc/init.d/Fnct.D

and loading the Lib first:

. /etc/init.d/Fnct.D/fnct_lib 