## Komodo JS Macro: Real auto word-wrap  
Originally published: 2012-04-08 13:00:46  
Last updated: 2012-04-10 17:38:13  
Author: Furlo   
  
This script will add real auto-wrap functionality to Komodo, ie. it will wrap text after reaching column 80 just in the same way as you would by pressing <Enter>.

You can bind a keyboard shortcut to macro, or trigger it on Komodo startup, or both. Either way, repeated pressing of binded shortcut (or running the macro) will switch it off and on again.

In fact, script only adds event listener, which fires a function (after each keypress), that checks if cursor position is not in column higher that 79 and, if needed, calls Komodo built-in function "Reflow paragraph" to reflow the paragraph.

This recipe was not created by me from scratch. I have just read David Brewer's feature request at [komodo-discuss](http://code.activestate.com/lists/komodo-discuss/4965/), used [troyt's original code](http://www.openkomodo.com/blogs/troyt/revenge-auto-wrap-type-type-type-ding) for autowrap and tweaked/simplified it a little.