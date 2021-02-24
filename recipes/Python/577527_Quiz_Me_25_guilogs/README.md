## Quiz Me 2.5 (gui_logs)  
Originally published: 2010-12-31 21:51:31  
Last updated: 2011-01-10 03:43:42  
Author: Stephen Chappell  
  
Before discovering http://quizlet.com/, the following program was developed for running custom quizzes to help with studying for college courses. The program is not very advanced, but it works reasonably well for what it was designed to do. If the program were developed further, it would need greater capabilities than it currently has and would require a secondary system for actually creating the quizzes (currently, they are hand-typed). Quiz Me could be a starting point for anyone who wishes to actually write a program such as this and inspire others to write much better programs than what this recipe currently offers.

There are several dialogs used throughout Quiz Me, and this module implements most of them. The standard dialog class in "tkinter.simpledialog" is modified slightly and used as a base class for the rest of the dialogs. ShowStatus displays whether a tier of the quiz is being entered or exited. AskQuestion allows questions to be asked and answered. ReviewProblems can be used to cycle through questions that were answered incorrectly. ShowReport gives a readout of the current cumulative progress score earned in the quiz. 