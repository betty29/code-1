## Partition Problem and natural selection  
Originally published: 2009-10-26 23:44:58  
Last updated: 2009-10-27 00:27:14  
Author: Jai Vikram Singh Verma  
  
Partition problem
From Wikipedia, the free encyclopedia

In computer science, the partition problem is an NP-complete problem. The problem is to decide whether a given multiset of integers can be partitioned into two "halves" that have the same sum. More precisely, given a multiset S of integers, is there a way to partition S into two subsets S1 and S2 such that the sum of the numbers in S1 equals the sum of the numbers in S2? The subsets S1 and S2 must form a partition in the sense that they are disjoint and they cover S. The optimization version asks for the "best" partition, and can be stated as: Find a partition into two subsets S1,S2 such that max(sum(S_1), sum(S_2)) is minimized (sometimes with the additional constraint that the sizes of the two sets in the partition must be equal, or differ by at most 1).

The partition problem is equivalent to the following special case of the subset sum problem: given a set S of integers, is there a subset S1 of S that sums to exactly t /2 where t is the sum of all elements of S? (The equivalence can be seen by defining S2 to be the difference S − S1.) Therefore, the pseudo-polynomial time dynamic programming solution to subset sum applies to the partition problem as well.

Although the partition problem is NP-complete, there are heuristics that solve the problem in many instances, either optimally or approximately. For this reason, it has been called the "The Easiest Hard Problem" by Brian Hayes.