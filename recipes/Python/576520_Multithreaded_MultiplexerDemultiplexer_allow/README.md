## Multithreaded Multiplexer/Demultiplexer to allow multiple transactions to be performed in parallel on a single channel  
Originally published: 2008-10-01 16:21:26  
Last updated: 2008-10-04 00:12:00  
Author: david decotigny  
  
Imagine you have one wire and you want to send a message from a machine A to another machine B, and wait for an answer from B (a "request/response transaction" in the following). Now imagine you have many threads on A which can make this kind of transaction "simultaneously", then you have to be cautious, otherwise you might get the wrong responses for your transactions. One solution is to serialize the transactions: the threads on A will have to wait for their turn to make their request/response transaction.

Another solution is to map a thread requesting a transaction on A, to a thread handling it on B. This allows for several transactions to be in flight at the same time on the same wire. This is what this module does: on A lives a multiplexer and threads call its transaction() method to initiate the request/response. On B, process_transaction() of a demultiplexer will get called by worker threads. All this in a multi-threaded way on a single wire. The module takes care of managing the interleaving requests/responses.