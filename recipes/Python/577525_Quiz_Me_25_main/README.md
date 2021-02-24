## Quiz Me 2.5 (main)  
Originally published: 2010-12-31 21:46:05  
Last updated: 2011-01-09 21:14:04  
Author: Stephen Chappell  
  
Before discovering http://quizlet.com/, the following program was developed for running custom quizzes to help with studying for college courses. The program is not very advanced, but it works reasonably well for what it was designed to do. If the program were developed further, it would need greater capabilities than it currently has and would require a secondary system for actually creating the quizzes (currently, they are hand-typed). Quiz Me could be a starting point for anyone who wishes to actually write a program such as this and inspire others to write much better programs than what this recipe currently offers.

This is the main entry point to the Quiz Me program. It creates the GUI context and sets the program up for automatic error logging. Experimental threading support is provided but unused in the program. Since the main application subclasses a frame, it can easily be embedded in another application without much difficulty. Quiz Me is entirely event based and has an event runner in the very last method shown here.