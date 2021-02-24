## How to Use Custom Dictionaries to Modify Attribute Lookup  
Originally published: 2006-01-25 10:07:16  
Last updated: 2006-01-25 19:26:50  
Author: Wolfgang Lipp  
  
some while ago, i posted a recipe with linked dictionaries (see <a href='http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/465748'>#465748</a>) to this site. yesterday a use case came up where that kind of delegational name/value lookup would be a nice thing if it worked for instance attributes.

basically, using a customized dictionary as an instance <tt>__dict__</tt> means modifying the standard lookup-by-inheritance-only behavior; in other words, part of the state of an instance can be kept in another instance.

this way, an instance that holds, say user configuration data, <tt>userCfg</tt> can be linked, at runtime, to a <tt>defaultCfg</tt> instance, and all the <tt>userCfg.frobfactor</tt> stuff that has not been defined by the user but for the default configuration would automatically be available.

unfortunately, the naïve approach (setting <tt>self.__dict__=MyDict()</tt> in <tt>__init__</tt>) fails to work. an inquiry to comp.lang.python was swiftly answered by bengt richter, who suggested to use a property for <tt>__dict__</tt>. i slightly improved on his suggestion by adding the capability to do item assignment as well.

note that since we are using <tt>__getattr__</tt> to redirect attribute lookup, delegation only happens <i>after</i> lookup in the method resolution order (mro) has failed (inheritance overrides delegation).