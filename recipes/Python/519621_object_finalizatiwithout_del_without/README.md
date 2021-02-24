## object finalization without __del__ and without hassles  
Originally published: 2007-05-07 07:59:59  
Last updated: 2007-05-11 09:32:33  
Author: Antoine Pitrou  
  
The well-known way to avoid __del__ (and its problems when the object to be deleted is involved in a reference cycle) is to use a finalization callback on a weakref.

This recipe simply makes it easier to write such "finalizable" objects by allowing to write the finalizer as a __finalize__ method (a bit similar to a __del__ method, but not exactly as we'll see).

The first step is to call the bind_finalizer(*attrs) method on your instance; you must give bind_finalizer a list of attribute names necessary for the finalizer to operate, and it will construct a "ghost object" holding those attributes (for example, if you have a "socket" attribute you want to close, you will include "socket" in the arguments to bind_finalizer, which in turn will bind a "socket" attribute on the ghost object). The ghost object has the same class as the original self, so you will be able to call instance methods and use class variables in the finalizer as well.

Please note: the ghost object is created and its attributes are bound *as soon as* bind_finalizer() is called, so their values must have been properly initialized. A practical idiom is probably to call bind_finalizer() at the end of your constructor. Creating the ghost ignores any __new__ or __init__ method you have defined, so you don't have to worry about constructor signature or unwanted side effects.

Your __finalize__ method must be written as a normal method, except that it can only access those instance attributes whose names you gave to bind_finalizer. This is because __finalize__ gets a "ghost instance" instead of the original instance.

Finally, there is a remove_finalizer() which does the obvious. Call it when the resources have been somehow freed manually and automatic finalization is not useful anymore.

With this recipe, you have an object-oriented finalization scheme which still works as required when your instance is part of a reference cycle to be broken by the Garbage Collector. Also, it doesn't use metaclasses which makes it easier to re-use if you have your own metaclasses.

You can find hereafter the code for the Finalizeable class, as well as an example TransactionBase class which helps writing objects with transaction-like behaviour and optional automatic rollback on object destruction.
(but the interesting stuff is really in Finalizable)