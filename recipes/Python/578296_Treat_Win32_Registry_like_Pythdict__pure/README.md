## Treat the Win32 Registry like a Python dict -- pure python  
Originally published: 2012-10-20 13:54:01  
Last updated: 2012-10-20 13:54:02  
Author: Grizzly Nyo  
  
This class wraps most of the win32api functions for accessing a registry. It will read and write all win32 registry types, and will de/serialize python objects to registry keys when a string or integer representation is not possible.

This is an update of recipe 573466, which is an update of 551761, which is in turn an update of 174627, folding in the enhancements listed in the discussion there to allow registry value types to be read and written within the dictionary metaphor if required. It doesn't change how it worked before, it adds a new capability, and shouldn't break existing code using the 551761 version.

Altered to use _winreg to avoid dependency on PyWin32 (not part of Python).