## Quickly add all dirs to sys.path if dir has .py file  
Originally published: 2012-04-06 01:27:34  
Last updated: 2012-04-06 16:06:17  
Author: Andrew Yurisich  
  
Add all dirs under `folder` to sys.path if any .py files are found.
Use an abspath if you'd rather do it that way.

Uses the current working directory as the location of using.py. 
Keep in mind that os.walk goes *all the way* down the directory tree.
