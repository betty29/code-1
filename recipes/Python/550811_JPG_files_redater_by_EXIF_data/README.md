## JPG files redater by EXIF data  
Originally published: 2008-03-04 01:34:39  
Last updated: 2014-12-11 10:07:39  
Author: Michal Niklas  
  
Iterates through a directory, reading the EXIF data from each jpg/jpeg file.
Parses the date/time from EXIF data and:
1. if it differs from file modification date/time then changes file date/time
2. moves file to `YYYY/YYYY_MM_DD` directory
