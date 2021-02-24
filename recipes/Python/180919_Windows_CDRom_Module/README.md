## Windows CDRom Module  
Originally published: 2003-02-14 14:18:53  
Last updated: 2003-02-14 22:20:55  
Author: Joel Lawhead  
  
This module provides easy control of cd drives on Win32 machines. Using the Python Win32 Extensions, the module automatically detects all cd drives and defaults to the first drive found or to a programmer specified drive. Methods include eject() to open the drive door, close() to close the drive door, and load() which tries to close the drive door and then make the drive available to the file system.

To test either import the WinCDRom module and create an instance of the Cdrom class:

import WinCDRom
cd = WinCDRom.Cdrom()
cd.eject()
cd.close()
cd.load()

Or just run the script from a DOS prompt to use the test function:

C:\python WinCDRom.py

Listing drives:
['D:']
Default drive: D:
Opening drive door...
Closing cd drive door... (CD read attempt will time out at 5 seconds.)
Loaded cd successfully in drive D:
WinCDRom Tests completed.