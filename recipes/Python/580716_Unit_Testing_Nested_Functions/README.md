## Unit Testing Nested Functions  
Originally published: 2016-11-10 09:21:38  
Last updated: 2016-11-10 10:23:11  
Author: Alfe   
  
Python allows the declaration of nested functions.  These are typically hard to unit test because using just the normal ways of calling they cannot be called from outside their surrounding function.  So they cannot be considered a clearly separated unit and thus cannot be unit tested.

This is a drawback of using them, so many developers (especially the ones deep into test driven development who strive to have a high unit test coverage) tend to avoid them in favor for standalone functions which can be called from the unit tests without any hassle.

But not all solutions with nested functions can be written as elegant with standalone functions.  Nested functions are powerful insofar that they can access the local variables of the surrounding function without any need to pass them into the nested function, thus the code can in many cases stay neat and tidy while using a standalone function instead might raise the need to pass the complete context in form of a bunch of parameters.  Also, using nested functions makes their local usage clear to any reader and keeps the name space tight.

But at least in the standard CPython (i. e. not necessarily in Jython, etc.) the implementation of functions (and methods) allows to find the nested function's code, wrap it properly to give it its needed context and then call it from the outside.  I wrote a small module which helps doing exactly this.