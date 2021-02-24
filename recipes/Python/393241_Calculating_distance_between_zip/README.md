## Calculating the distance between zip codes  
Originally published: 2005-03-29 19:14:04  
Last updated: 2006-04-25 20:40:00  
Author: Kevin Ryan  
  
I came across the mention of a formula labeled "The Great Circle Distance Formula" that purported to calculate the distance between any two points on the earth given their longitude and latitude points (the reference was in a Linux Magazine article).  So, I looked up some information and cooked up a Python version of the calculation.  There are references in the code where you can obtain approximate zip code data for free (e.g., if you wanted to enhance your website by adding a "Search within x mi's" feature), as well as references to the GCDF if you have further interest.  Enjoy!

04/25/2006 update: I've decided to update this recipe with an object oriented bent where the information is cached once the object is instantiated.  I've also added command line access to automatically download the zipcode file from the census website (just use 'python zips.py -d' and it will download a copy to your harddrive under 'zips.txt').  Lastly, I've added some unit testing so that if any future changes are made this will automatically run and tell me if anything pops out as wrong.