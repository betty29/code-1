## Interleaving Sequences  
Originally published: 2007-04-18 23:23:26  
Last updated: 2007-04-18 23:23:26  
Author: Richard Harris  
  
Interleaving can be thought of as two-dimensional iteration over a sequence of sequences, pulling the ith element from all n seqeuences before moving on to the ith + 1 element. Interleave does not truncate to the shortest list unlike flatten(zip(seqA, seqB)) [see flatten() recipe]. Here's an illustration:

    a = [1,3,5]
    b = [2,4,6,8]
    c = ["x","y","z"]

interleave(a,b,c) will return:

    [1, 2, "x", 3, 4, "y", 5, 6, "z", 8]