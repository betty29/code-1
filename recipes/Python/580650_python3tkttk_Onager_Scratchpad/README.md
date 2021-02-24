## [python3-tk/ttk] Onager Scratchpad  
Originally published: 2016-04-24 02:17:38  
Last updated: 2016-04-24 02:34:03  
Author: Mickey Kocic  
  
I wrote this simple text editor to use for my diary. It's customized the way I like it, but the code is set up so it's easy for other people to change bg, fg, font, etc. I've also compiled a standalone Windows executable (thank you very much ActiveState! without ActivePython the compilation would have been impossible). Anyone who wants a copy of the executable is free to message or email me.

NOTE: If you get an error that the theme is not recognized, just comment out line 18 or run the following code in your python3 interpreter:

    >>>from tkinter.ttk import Style
    >>>s = Style()
    >>>s.theme_use()

You'll get a list of the available themes and can replace the 'alt' in line 18 with any one of them you want.