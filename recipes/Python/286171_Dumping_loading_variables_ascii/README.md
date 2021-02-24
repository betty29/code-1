## Dumping and loading variables in ascii format  
Originally published: 2004-06-28 11:32:57  
Last updated: 2004-07-22 18:07:39  
Author: Karthikesh Raju  
  
Dump and load variables for exchanging data between matlab and numarray.
The variables are in a dictionary, and each key in the variable gets
dumped into a file named after the variable. If the variable is complex,
the real and imag parts are dumped into separate files.

Loading of files, created by matlab is also possible. In this case, the returned dictionary has the keys derived from the file names and values from the files.