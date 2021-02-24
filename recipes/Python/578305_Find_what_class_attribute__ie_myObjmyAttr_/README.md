## Find what class an attribute - ie, myObj.myAttr - comes from, and how it's defined  
Originally published: 2012-10-26 12:55:29  
Last updated: 2012-10-26 12:59:47  
Author: Paul Molodowitch  
  
When inspecting new code (or when debugging), it can be handy to know exactly where a given attribute on an object or class comes from.

As a simple example, if you have a class MyClass, you might want to know where MyClass().myMethod is defined.

However, things can get tricky when things like __getattr__, __getattribute__, or even compiled objects come into play.  That's where this function comes in.  It returns what class a given attribute comes from, and what method was used to define it - ie, '__dict__' ('normal' definitions), '__slots__', '__getattr__', '__getattribute__', '(BUILTIN)'.

(Note - this function should't be relied on to be 100% accurate - rather, it's a best guess, for where to look to find it.  It takes some pretty infrequent edge cases for it to be wrong, though...)