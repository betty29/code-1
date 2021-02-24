## Use Candygram to communicate among threads.  
Originally published: 2004-08-27 12:14:37  
Last updated: 2004-08-27 12:14:37  
Author: Michael Hobbs  
  
With the Candygram package [ http://candygram.sourceforge.net ], developers can send and receive messages between threads using semantics nearly identical to those in the Erlang language [ http://www.erlang.org ]. Erlang is widely respected for its elegant built-in facilities for concurrent programming.

The beauty of the Erlang system is that it is simple and yet powerful. To communicate with another thread, you simply send a message to it. You do not need to worry about locks, semaphores, mutexes, etc. to share information among concurrent tasks. Developers mostly use message passing only to implement the producer/consumer model. When you combine message passing with the flexibility of a Receiver object, however, it becomes much more powerful. For example, by using timeouts and message patterns, a thread may easily handle its messages as a state machine, or as a priority queue.

For those who wish to become more familiar with Erlang, http://www.erlang.org/download/erlang-book-part1.pdf [Concurrent Programming in Erlang] provides a very complete introduction. In particular, the Candygram package implements all of the functions described in chapter 5 and sections 7.2, 7.3, and 7.5 of that book.