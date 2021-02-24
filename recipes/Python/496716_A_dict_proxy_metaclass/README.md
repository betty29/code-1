## A dict proxy metaclass.  
Originally published: 2006-05-17 04:05:43  
Last updated: 2006-05-17 04:05:43  
Author: Sundance Greydragon  
  
This recipe creates a metaclass, that can be used in any dict-like object to map specially named attributes to keys of that dictionary.

By default, such attributes are those whose name begin with one (and only one) underscore, and they are mapped to the dictionary key of the same name, without the underscore; but the method to determine that behavior is overridable.

For instance, accessing:
  d._somekey
would return:
  d.["somekey"]

Creation, update and deletion of such attributes works as expected.