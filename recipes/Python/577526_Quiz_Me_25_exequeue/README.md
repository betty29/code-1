## Quiz Me 2.5 (exe_queue)  
Originally published: 2010-12-31 21:49:21  
Last updated: 2011-01-09 21:19:15  
Author: Stephen Chappell  
  
Before discovering http://quizlet.com/, the following program was developed for running custom quizzes to help with studying for college courses. The program is not very advanced, but it works reasonably well for what it was designed to do. If the program were developed further, it would need greater capabilities than it currently has and would require a secondary system for actually creating the quizzes (currently, they are hand-typed). Quiz Me could be a starting point for anyone who wishes to actually write a program such as this and inspire others to write much better programs than what this recipe currently offers.

The Pipe and _Method classes presented here are for providing optional thread support to the tkinter GUI library. Oftentimes, it can be inconvenient to play with threads and GUI libraries simultaneously, and most GUI libraries require GUI specific operations to be performed within a certain thread. The classes below are for wrapping the root of the application so that method calls can be executed at a later time within whatever thread they are supposed to be executed in. This program was used as a test platform of the concept though it did not see any of its expected use: threading is not used in this application.