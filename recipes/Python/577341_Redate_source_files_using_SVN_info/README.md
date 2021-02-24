## Redate source files using SVN info from $Id:$  
Originally published: 2010-07-30 10:00:25  
Last updated: 2010-07-30 10:00:25  
Author: Michal Niklas  
  
Iterates through a directory, reading the data from svn info that looks like:

    $Id: svn_redater.py 747 2010-07-30 09:56:08Z mn $

from source files.

Parses the datetime from svn info and if it differs from file
modification datetime then changes file datetime
