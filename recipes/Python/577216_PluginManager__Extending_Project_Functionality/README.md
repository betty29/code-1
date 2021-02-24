## PluginManager - Extending Project Functionality By Using Custom Modules/Plugins On The Fly.  
Originally published: 2010-05-05 21:16:46  
Last updated: 2010-05-07 15:32:10  
Author: AJ. Mayorga  
  
This demo shows how you can create and manage your own custom plugins for extending functionality in your Python projects. There are no safety wrappers in this demo for restricting plugins aside from that fact that plugins are run as an extention of a management class which is run in its own instance only receiving data passed to it by the RumModules method, that said security should ideally be applied to the ModuleAPI class, by restricting __builtins__ on eval calls and/or validating plugin content and parameters which can be done by extending the Prepaser Class. For a great recipe/demo of restricting eval call see http://code.activestate.com/recipes/496746. 

That aside it was alot of fun to write and use. Enjoy

PS: you will need http://code.activestate.com/recipes/577144/ to import Xceptions