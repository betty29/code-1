## Metaclass for Interface Checking  
Originally published: 2003-06-09 01:03:35  
Last updated: 2003-06-12 02:00:39  
Author: Raymond Hettinger  
  
Checks a class definition for required attributes
<br>
To use it, add two lines to your class, __metaclass__=InterfaceChecker and __implements__=[InterfaceName].  The example below generates the following error message:
<br>
InterfaceOmission: ['__delitem__']
<br>
Verifying interfaces for an object becomes trivial.  For instance, if you need to validate that variable 'x' implements a minimal sequence interface, verify that: <br>
MinimalSequence in x.__implements__