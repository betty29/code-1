## Generating random intergers within a range of max & min.  
Originally published: 2003-03-04 09:58:21  
Last updated: 2003-03-04 09:58:21  
Author: Dom Lam  
  
Here's an example on how to generate a random number between 2 numbers
Based on C code,
algorithm = randomNumber % ((max + 1) - min) + min
Here's the tcl version using rand():
*note
Change 100 to 1000 if you want a random number that goes into thousands. etc..
Also the rand() function generates a number between 0 & 1.
That's why one would multiply by 10 or 100 or 1000, etc..