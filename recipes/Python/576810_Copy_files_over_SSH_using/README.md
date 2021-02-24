## Copy files over SSH using paramiko  
Originally published: 2009-06-16 05:21:53  
Last updated: 2015-12-06 14:19:15  
Author: ccpizza   
  
This script copies files in unattended mode over SSH using a glob pattern. It uses the [paramiko](http://www.lag.net/paramiko/) module behind the scenes. It operates as an actual SSH client, and does *not* rely on any command line utilities, such as `scp`.

It first tries to connect using a key from a private key file or from an SSH agent. If RSA authentication fails, it will try to authenticate with a password if passwords are allowed on the SSH server.
Assumes the `rsa_private_key` was generated with an empty passphrase.

On most linux/unix-like systems paramiko can be installed with `sudo easy_install paramiko` or `pip install paramiko` or using the built-in system package manager.

See also http://www.paramiko.org/installing.html