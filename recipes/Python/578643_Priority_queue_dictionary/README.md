## Priority queue dictionary  
Originally published: 2013-08-18 07:45:01  
Last updated: 2013-08-25 00:23:12  
Author: Nezar Abdennur  
  
An indexed priority queue implemented in pure python as a dict-like class. It is a stripped-down version of [pqdict](https://pypi.python.org/pypi/pqdict/). A Priority Queue Dictionary maps dictionary keys (dkeys) to updatable priority keys (pkeys).

The priority queue is implemented as a binary heap, which supports:    
     
- O(1) access to the top priority element        

- O(log n) removal of the top priority element     

- O(log n) insertion of a new element

In addition, an internal dictionary or "index" maps dictionary keys to the position of their entry in the heap. This index is maintained as the heap is manipulated. As a result, a PQ-dict also supports:          

- O(1) lookup of an arbitrary element's priority key     

- O(log n) removal of an arbitrary element          

- O(log n) updating of an arbitrary element's priority key

A data structure like this can be used to drive simulations, schedulers, certain greedy algorithms, merging streams of sorted data, and other applications where priorities may need to be changed frequently.