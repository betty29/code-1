## Convenience 'timeit' function  
Originally published: 2005-01-01 12:39:04  
Last updated: 2005-01-12 15:12:04  
Author: m k  
  
This function makes it easier to use the timeit module from the interactive interpreter.

Just specify function with (optional) arguments to run, optional number of runs, and optional name of module (which if not specified defaults to the name of the function).

Example:

>>> timefunc.timefunc('r()', 20)
20 loops, best of 3: 6.91e+004 usec per loop

>>> timefunc.timefunc('rx()', 20, 'r')
20 loops, best of 3: 2.23e+004 usec per loop