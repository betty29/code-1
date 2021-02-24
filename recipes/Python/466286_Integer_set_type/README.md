## Integer set type  
Originally published: 2006-01-12 07:28:50  
Last updated: 2006-01-23 15:07:55  
Author: Heiko Wundram  
  
While programming an IPv4-Range class I stumbled upon the need for an efficient integer set type, which doesn't store individual items like the builtin set type does, but which only stores longs and ints, and does this in a run length encoded way to save space.

The following class implements such a beast as an immutable type, amongst support for minus and plus infinity to allow you to create infinitely sized sets. The set supports almost all operations that the builtin set type supports (which means excluding rich comparisons __gt__, __ge__, etc., for which I could find no meaningful interpretation).

The recipe is somewhat longish, but I couldn't think of some more elegant way to express most operations than by using predicate logic together with a set iterator, which keeps runtime for all set operations in O(n), except normalization, which is O(n*logn) because of the sort() operation on the list of ranges. Normalization is only done once on construction of the set; when a set is combined by some operation with another set, the output is automatically normalized.

The _Infinity private type is required to facilitate comparisons. _Infinity(True) will be smaller than any number and equal to itself, _Infinity(False) bigger than any number and equal to itself. This makes sorting easier.