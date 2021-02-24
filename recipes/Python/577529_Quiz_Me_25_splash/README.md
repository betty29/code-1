## Quiz Me 2.5 (splash)  
Originally published: 2010-12-31 21:54:16  
Last updated: 2011-01-10 04:05:50  
Author: Stephen Chappell  
  
Before discovering http://quizlet.com/, the following program was developed for running custom quizzes to help with studying for college courses. The program is not very advanced, but it works reasonably well for what it was designed to do. If the program were developed further, it would need greater capabilities than it currently has and would require a secondary system for actually creating the quizzes (currently, they are hand-typed). Quiz Me could be a starting point for anyone who wishes to actually write a program such as this and inspire others to write much better programs than what this recipe currently offers.

Splash provides an easy mechanism for displaying a splash screen as the "Quiz Me" program is starting up. This recipe has been published elsewhere on the Python Cookbook, but is included here for completeness in the layout of the program. The class's constructor takes the root of the application, the path to the logo to be displayed (usually a GIF image), and a minimum amount of time for the splash screen to be displayed. Used as a context manager around initialization code makes this a very easy class to use, and it will automatically clean up after itself when it has finished doing its job.