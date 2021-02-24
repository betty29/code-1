## socket.recv -- three ways to turn it into recvall  
Originally published: 2005-04-01 18:07:29  
Last updated: 2005-04-05 13:47:57  
Author: John Nielsen  
  
An issue with socket.recv is how to know when you are done receiving data.  A TCP stream guarantees the bytes will not arrive out of order or be sent more than once. But you do not know the size of the data that will be sent to you. 100 bytes could be sent as group of 10 bytes or maybe in one shot. Ultimately, this means you have to use a loop in some fashion until you know it is done.

The basic recv returns an empty string when the socket is disconnected.
From that you can build a simple loop that will work as long as the sender manages to disconnect the socket at the appropriate time. However, there could be situations where a local error will mask as a clean shutdown or maybe a close() is never called.

Three very basic methods are shown below that try to fix that problem. They use either a time-based, end marker, or size of payload method. Since you cannot be sure just what you are going to receive, you have to be careful that you get enough of a message to determine the size of payload or end marker.

I updated the recv_size method to allocate data in larger chunks if it gets a large stream of data, which can increase performance.