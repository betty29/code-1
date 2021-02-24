## Parse call function for Py2.6 and Py2.7   
Originally published: 2009-02-26 19:37:55  
Last updated: 2009-02-28 20:13:15  
Author: Jervis Whitley  
  
In some cases it may be desirable to parse the string expression "f1(*args)"
and return some of the key features of the represented function-like call. 

This recipe returns the key features in the form of a namedtuple. 

e.g. (for the above)

    >>> explain("f1(*args)")
    [ Call(func='f1', starargs='args') ]

The recipe will return a list of such namedtuples for `"f1(*args)\nf2(*args)"`
Note that while the passed string expression must evaluate to valid python syntax, 
names needn't be declared in current scope.


