## groupby() For Unsorted Input  
Originally published: 2017-05-12 10:33:22  
Last updated: 2017-05-12 10:40:58  
Author: Alfe   
  
We all know the `groupby()` which is available in the `itertools` standard module.  This one yields groups of consecutive elements in the input which are meant to be together in one group.  For non-consecutive elements this will yield more than one group for the same key.

So effectively, `groupby()` only reformats a flat list into bunches of elements from that list without reordering anything.  In practice this means that for input sorted by key this works perfect, but for unsorted input it might yield several groups for the same key (with groups for other keys in between).  Typically needed, though, is a grouping with reordering if necessary.

I implemented a likewise lazy function (yielding generators) which also accepts ungrouped input.