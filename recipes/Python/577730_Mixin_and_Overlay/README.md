## Mixin and Overlay  
Originally published: 2011-06-01 05:05:25  
Last updated: 2011-06-01 05:16:47  
Author: Eric Snow  
  
The Two Sides of Classes
========================

Class inheritance either adds new attributes to a class, or changes existing attributes.  However, this distinction is not made in Python's class system.  This recipe is a stab at providing that separation.  It takes advantage of metaclasses and class decorators to do it.

For this recipe the two sides of class inheritance are called mixins and overlays.  Mixins add new attributes to a class.  Overlays change existing attributes, which in the case of methods means changing the behavior of the methods.  However, overlays do not add any attributes.

Separation of Concerns
======================

Another issue with class inheritance is that abstraction rarely breaks down into perfect trees with a clear separation of concerns.  Python allows multiple inheritance, which can help, but requires cooperation between classes in the diamond hierarchy.  Mixins and overlays help with this problem.  Hopefully, that will be evidenced by the recipe and subsequent examples.

With this approach, the main single inheritance line can focus on the core abstraction and mixins/overlays can be used to extend the classes in other directions.  This does not solve all the problems regarding separation of concerns, but it solves some.  I hope to address the rest in another recipe that centers around delegation through a component architecture on instances.

Interfaces
==========

Since Python 2.6 we have had Abstract Base Classes providing a mechanism for promising what interfaces an object provides.  I'll show in one of the examples how an ABC can be split into a interface portion and a mixin portion.  The recipe takes advantage of the ABC functionality in the Python type system.  I expect that mixins and overlays would be a good fit with one of my other recipes (Recipe 577711).

The Recipe Classes
==================

This recipe provides a standard approach to applying mixin classes without using inheritance.  This is done through a metaclass.  The metaclass builds a __mixins__ attribute on the class and provides a mixes_in class decorator.  Applying that decorator to the class will add the attributes in __mixins__ to the decorated class.  However, if any of those names are already bound on the name then it will fail.  The decorator returns the modified class.

**Note**: Traditional mixins are typically done through multiple inheritance, as opposed to class decorators.

This recipe also provides a companion to mixin classes, called overlays.  This is done through a metaclass in exactly the same way as the mixins, but provides an __overlays__ attribute and a class decorator called overlays.  In contrast to mixins, if an overlay attribute is missing on the decorated class, it will fail.  This is because the decorator will return a new class that inherits from the decorated class, and overrides the attributes in __overlays__.


**Note**: Metaclasses are used here because we need to pull from the class namespace there.  A class decorator does not afford us the same functionality without more complexity.

**Note**: This recipe should work fine in 2.7 with a switch to the __metaclass__ syntax.