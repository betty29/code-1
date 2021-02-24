## Accented Characters for Tkinter Widgets  
Originally published: 2009-11-07 18:29:44  
Last updated: 2011-01-07 13:09:51  
Author: Stephen Chappell  
  
See Recipe 286155 for original code and author.

This module provides two standard Tkinter widgets, Entry and ScrolledText, modified for text editing with key bindings that allow entering accented letters, umlauts, etc.

Usage: To enter an accented character, press Ctrl-symbol, then press the character key. Example: to enter U with umlaut, press Ctrl-", U. For accent symbols that need shift, press Ctrl-Shift-symbol (for example, Ctrl-Shift-' if " is under Shift-').

Accent bindings are defined in the Diacritical.accent table. Not all accents exist on all letters. This is handled by gracefully falling back to the base letter.

Additional changes in default Tk key bindings: Ctrl-A is now select-all.