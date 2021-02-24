## Easy attribute setting and pretty representation  
Originally published: 2014-12-02 14:29:18  
Last updated: 2014-12-03 09:55:06  
Author: Joakim Pettersson  
  
Mix in one or more of these classes to avoid those tedious lines of administrative code for setting attributes and getting useful representations. 

If you inherit HasInitableAttributes, your should be able to obj = eval(repr(obj)) without loosing data.

enthought.traits.api.HasTraits seems to mix in well also.