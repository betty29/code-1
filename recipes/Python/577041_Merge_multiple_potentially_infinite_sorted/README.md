## Merge multiple (potentially infinite) sorted inputs into a single sorted output  
Originally published: 2010-02-11 01:08:04  
Last updated: 2010-04-01 04:54:16  
Author: Gabriel Genellina  
  
Merge a (possibly infinite) number of already sorted inputs (each of possibly infinite length) into a single sorted output.

Similar to heapq.merge and sorted(itertools.chain(*iterables)).

Like heapq.merge, returns a generator, does not pull the data into memory all at once, and assumes that each of the input iterables is already sorted (smallest to largest).

Unlike heapq.merge, accepts an infinite number of input iterables, but requires all of them to come in ascending order (that is, their starting point must come in ascending order).

In addition, accepts a *key* function (like `sorted`, `min`, `max`, etc.)
