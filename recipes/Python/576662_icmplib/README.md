## icmplib  
Originally published: 2009-02-22 10:48:00  
Last updated: 2009-02-22 10:48:00  
Author: cerebus mindless  
  
[main author Brett Cannon]
[co-authored with Philip E. Nu�ez]
[ported to python3k by cerebus_mindless]

Python's stdlib does not have any included library for supporting ICMP packets; both reading them or creating them. But ICMP packets are common and useful; they are used for both the traceroute and ping utilities. And thus they can be useful to control to do network diagnostics.

The Packet class is what is used to create and read ICMP packets. To create a packet you instantiate the class, set the header and data fields, and then call the create() method which will the string representation that can be passed to a socket.

To read a packet, use the Packet.parse() classmethod, which will return an instance of Packet with the fields filled out.

To show its use you can also see the ping() method that is included. Just use the code as a script and pass in an address to ping. Response time is printed to stdout.

One word of warning, though, when using this module. Raw sockets tend to require root permissions on the process. Thus you might need to use sudo to execute the Python interpreter to make this all work. ping() does drop sudo permissions as soon as it can, though, for security reasons.