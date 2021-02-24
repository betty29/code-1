## Python Exception Chains (or Trees)  
Originally published: 2012-09-04 15:57:51  
Last updated: 2013-02-04 15:15:22  
Author: Alfe   
  
I have here an approach for chaining exceptions in case a lower layer (*library*) raises an exception which is caught in an upper layer (*application*) and later given as *cause* when a different exception is raised.  Passing this *cause* exception is meant to offer access to the stack trace of the inner exception for debugging.

This approach is implemented in Python 3 and in Java, so it definitely makes sense; you also quickly find questions on [Stackoverflow](http://stackoverflow.com) concerning it.

I even extended this feature by not only using chains of exceptions but also trees.  Trees, why trees?  Because I had situations in which my application layer tried various approaches using the library layer.  If all failed (raised an exception), my application layer also raised an exception; this is the case in which I wanted to pass more than one cause exception into my own exception (hence the tree of causes).

My approach uses a special Exception class from which all my exceptions will inherit; standard exception must be wrapped (directly after catching, to preserve the exception stack trace).  Please see the examples contained in the code below.  The exception itself is rather small.

I'd be happy to hear any comments regarding memory leaks (I didn't find any but one never knows), usability, enhancements or similar.