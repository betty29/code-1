## CallQueue: Easy inter-thread communication  
Originally published: 2006-04-21 05:25:27  
Last updated: 2006-04-22 08:52:08  
Author: R K  
  
A framework for easy (2-way) inter-thread communication resembling normal function calling.

Especially useful for non-blocking UI techniques and for load distribution on jerky resources. Can replace stiff Queue.Queue techniques in most cases - making threading code more readable and functional.

CallQueue lets you express function directly in local context, but execute things in a target thread. It focuses naturally on 2-way communication (with return value responses) and includes a fluid concept for inter-thread exception (transfer) issues. Supports also multi-producer, multi-consumer communication.

A target thread just has to do callqueue.receive() periodically without worrying about any data passing. Thus CallQueue also supports naturally a high-level bulk threading concept with anonymous "default consumer threads": Allocated "thread resources" can be thrown efficently on bunches of jobs.