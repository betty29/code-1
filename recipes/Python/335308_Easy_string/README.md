## Easy string interpolation in Python 2.4  
Originally published: 2004-11-12 02:46:30  
Last updated: 2004-11-12 02:46:30  
Author: Michele Simionato  
  
Regular string interpolation in Python requires the user to pass an explicit
keyword dictionary. This recipe adds a little bif of magic, so that if
a name is not found in the passed dictionary, it is looked up in the
locals and globals dictionaries. It is also possible not to pass any
explicit dictionary, then the names is searched in the locals and globals
dictionaries only.