## Search nth smallest element in really big file  
Originally published: 2010-11-30 07:31:57  
Last updated: 2010-11-30 17:38:38  
Author: Teodor Kichatov  
  
Search nth smallest float in really big file (more, more and more bigger than available RAM)
in a single pass through the file

if your file more than 150GB - you should use a more appropriate sampling params to the data
more - you can use tempfile to store data(interval) returned from func fill_interval
data:
file with only one float number per line, good shuffled

