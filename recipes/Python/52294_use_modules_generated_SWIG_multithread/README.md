## use modules generated with SWIG in a multi-thread environment  
Originally published: 2001-03-21 15:43:24  
Last updated: 2001-03-21 15:43:24  
Author: Joe VanAndel  
  
To use multiple threads, you must release the Python thread-lock.
The simplest way with SWIG is to use an except directive.For example,
Mark Hammond does the following in the Win32 extensions: