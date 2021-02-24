## Generating Code Coverage HTML Output  
Originally published: 2006-04-20 09:56:42  
Last updated: 2010-10-17 15:17:44  
Author: Sebastien Martini  
  
Code coverage testing is very useful especially for dynamic languages, it can easily give a view of the unused parts of your code. Not that this method is able to prove that statements are dead code, but instead help to prevent from syntax errors and to force yourself to think about your code, to find the right test cases reaching the unused statements.

In that sense, the module [coverage.py](http://www.nedbatchelder.com/code/modules/coverage.py) made by [Ned Batchelder](http://www.nedbatchelder.com) is very useful and efficient.

The analysis returned by this module is very accurate, but as unreached lines numbers are not very readable by itself, this recipe simply generate an html output highlighting unreached lines. This recipe is directely based upon a [source code colorizer](http://chrisarndt.de/en/software/python/colorize.html) derived from [this](http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/52298) recipe.
