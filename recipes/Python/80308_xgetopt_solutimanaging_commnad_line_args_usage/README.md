## xgetopt: a solution for managing commnad line args and usage information  
Originally published: 2001-10-07 19:37:32  
Last updated: 2001-10-14 05:33:43  
Author: Alan Eldridge  
  
The getopt module, like GNU getopt/getopt_long, separates short and long options, and makes no way to coordinate options with usage messages. This leads to an opportunity for usage info and the actual options to diverge, and makes it harder to see, at a glance, what short and long options correspond to one another. It also leaves handling of preset or default options up to ad-hoc solutions, often the same or similar code implemented time and time again. Xgetopt addresses all of these concerns in a simple, easy to use module.This code requires my word_wrap.py module, which is also posted to the Python Cookbook following this module.