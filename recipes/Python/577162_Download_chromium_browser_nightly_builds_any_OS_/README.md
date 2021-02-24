## Download chromium browser nightly builds for any OS (with proxy support)  
Originally published: 2010-03-29 10:49:40  
Last updated: 2014-07-05 18:47:47  
Author: ccpizza   
  
Downloads the latest Chromium browser build from http://commondatastorage.googleapis.com/chromium-browser-continuous/ using urllib2 or wget (with Python versions below 2.5) and unzips the downloaded zip file to a predefined folder.
 
To use a custom proxy define the `HTTP_PROXY` system variable.

The script will figure out the OS but you can also pass the platform as the first parameter (one of ` win32, linux, linux64, mac`).

*Prerequisites (!! only for Python versions below 2.5):*

* `wget` - usually already installed on most linux systems. Windows users can get it [here](http://gnuwin32.sourceforge.net/packages/wget.htm).

* `unzip` - used for unpacking the archive; usually already installed on most linux systems. Windows users can get it [here](http://gnuwin32.sourceforge.net/packages/unzip.htm).

Both `wget` and `unzip` should be available in PATH (for Python 2.5+ native Python modules are used).

For most Linux distros this script does not make much sense since the built-in package managers do a better job of managing chromium builds and dependencies, but it still can be useful if you are using a stable Chromium build but would like to be able to test the nightly builds too.

For OSX an additional installation step will be performed using the `install.sh` that is included in the OSX build. The OSX installer will copy the package to `~/Applications/Chromium`, and set some permissions that are required for Chromium to run. Running the unpacked zip without doing the installation will most likely will not work because of missing executable permissions on some files.