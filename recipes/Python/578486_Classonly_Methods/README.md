## Class-only Methods  
Originally published: 2013-03-07 19:55:04  
Last updated: 2013-03-08 17:00:53  
Author: Eric Snow  
  
We use the classmethod builtin to tie methods to the class rather than the instance.  This is really useful for a variety of things, like alternate contructors.  However, sometimes you don't want to expose the method on the instances, just on the class.

For instance, it usually doesn't make a lot of sense to have direct access to alternate constructors from instances; the main constructor, via the __call__ method, is only available on the class.  Why?  So that instances call implement their own call semantics.  This is similar to why the methods (and other class attributes) on namedtuples all have names starting with an underscore.

To restrict a method just to the class, currently you must use a metaclass.  Most people consider this black magic so they just use @classmethod.  Furthermore, implementing a metaclass is simply more verbose than decorating a method with classmethod.  Plus you have to deal with things like metaclass conflicts and the fact that metaclasses are inherited.

So...here is a sibling to classmethod that makes a method class-only without introducing metaclass complexity.  You use it the same way as you would classmethod.