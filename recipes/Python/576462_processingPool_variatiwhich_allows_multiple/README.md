## processing.Pool variation which allows multiple threads to send the same requests without incurring duplicate processing  
Originally published: 2008-08-29 00:30:39  
Last updated: 2008-09-17 17:01:21  
Author: david decotigny  
  
processing.Pool (http://pypi.python.org/pypi/processing) is a nice tool to "parallelize" map() on multiple CPUs.
However, imagine you have X threads which send the same request Pool.map(getNthPrimeNumber, [100000, 10000000, 10000]) at (almost) the same time. Obviously, you don't want to compute X times getNthPrimeNumber for 100000, 10000000, 10000... unless you have 3.X processors available. You would like one thread to submit the 3 requests, and then the X-1 others would notice that the requests have already been submitted and will then just wait for the result.
This is what this code is about: a kind of "trensient memoize" for processing.Pool::imap().