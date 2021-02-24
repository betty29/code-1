## An easy password generator using standard Python modules  
Originally published: 2005-09-16 02:06:28  
Last updated: 2006-11-12 11:54:30  
Author: hemanth sethuram  
  
This recipe generates a password of any length using the standard library modules of Python. The password generated is a function of an identifier and a master password.

I liked the idea behind the PasswordMaker browser plugin (http://passwordmaker.org/). But I wanted to have a portable command line version which I wanted to carry around without having the need to install an application or needing a web browser. Additionally I wanted to use only the pre-installed modules.
I haven't looked into the PasswordMaker's algorithms but I have borrowed the main idea that you have a single master password. To that you add a site address or your account name and take a cryptographic hash (MD5, SHA-1, etc.) of this string. Your password will be a function of this generated hash.
I have broken each of the above steps into separate functions so that one can replace the actual implementation with their own algorithms.
Note on Security: I am not a security expert; so I am not qualified to comment on how secure this approach is. I welcome others' comments on the vulnerabilities.