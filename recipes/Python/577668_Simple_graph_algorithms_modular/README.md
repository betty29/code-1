## Simple graph algorithms with a modular design  
Originally published: 2011-04-20 01:11:45  
Last updated: 2011-04-21 13:40:32  
Author: jimmy2times   
  
The purpose of this recipe is to look at algorithmic graph theory from an object-oriented perspective.

A graph is built on top of a dictionary indexed by its vertices, each item being the set of neighbours of the key vertex.
This ensures that iterating through the neighbours of a vertex is still efficient in sparse graphs (as with adjacency lists) while at the same time checking for adjacency is expected constant-time (as with the adjacency matrix).

Any valid class of graph must implement the interface defined by AbstractGraph.

A generic search algorithm takes as input a graph, source and target vertices and a queue.
A queue must implement the methods Q.get(), Q.put() and Q.empty() in such a way to get the desired order in visiting the vertices.

Given this pattern, breadth-first and depth-first search are essentially defined by the corresponding expansion policies: the first one uses an actual FIFO queue, the second one a LIFO queue (or stack).