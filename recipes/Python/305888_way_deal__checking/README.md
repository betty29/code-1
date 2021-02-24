## A way to deal with  checking for types  
Originally published: 2004-09-25 10:29:57  
Last updated: 2004-09-28 11:17:30  
Author: John Nielsen  
  
Managing types is normally simple in python, since it does typing as late as possible during runtime. Sometimes the issues of type still rears it's head, especially among programmers used to the "type at compile time" variants.

You want to resist doing a naive approach like type(obj)==str, since you then ignore subclasses.

What this recipe does is make a distinction between objects that _are_ are certain type or it's subclass and objects that act good enough. Most of the time
the difference will not matter. If it is a certain python type or in some cases like with a sequence, possible among a few python types, it returns a 1, if it is good enough it returns a -1, and finally it returns zero if it is not good enough.

Good enough is enabled by checking for attributes and callables instead of explicit type and sometimes by checking for success of certain actions. In cases where it can be good enough, you simply check for just a true value which both 1 and -1 will evaluate to.

I put in typical checks for many things ranging from generators to lists to file handles.