## The End of Inheritance: Automatic Run-time Interface Building for Aggregated Objects  
Originally published: 2002-09-15 16:20:13  
Last updated: 2002-09-15 16:20:13  
Author: Paul Baranowski  
  
"Design Patterns" [GoF] prescribes two commandments to live by:

1) Program to an interface, not an implementation.
2) Favor object composition over class inheritance.

This implies that every class should have a defined interface, and that every class should be a composition of objects.  However, there is often a large barrier to object composition - sometimes a class needs to have the interface of its components.  You don't want to extend the functionality of the component, you just want its interface, and you want all calls to that interface to be sent to the component object.  In this case, it is so much easier to inherit even though you are not really extending the functionality of the parent class (this especially happens when writing GUI applications, where the components have huge APIs).  If you bite the bullet and make a composite, you end up writing a lot of wrapper functions (see Figure 1).  (A wrapper function has the same function signature as the function it is wrapping, and it simply calls the same function in the target object.)  No one likes to write wrapper functions - its dull, boring, menial work.  I've thrown out plenty of my own designs because they would have required me to write wrappers for a huge number of functions (for example, the wxWindow class has over 130 member functions. See http://www.wxWindows.org), so I end up inheriting even though I know it is "wrong".

There is no way around this problem in C++ and Java (though maybe an IDE vendor could put in a tool to automatically generate wrapper functions).  Amazingly enough, however, Python allows you to modify classes at run time.  This means it is possible to make Python automatically write these wrapper (or proxy) functions for you.