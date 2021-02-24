## Paster Run Script  
Originally published: 2011-04-20 13:22:48  
Last updated: 2011-04-20 13:22:49  
Author: Nick Holden  
  
If you are like me and your company has a custom piece of software for managing processes, you have your paster app installed in egg form in a virtualenv, then you might have a hard time running a paster server (turbogears 2) within those limits.

As I had so much trouble writing this I thought I would share. You can add this as a console script in your egg, then run it as --prod or --dev. When run as --prod it adds a signal handler so that if it is sigtermed by the "supervisor" program then it will kill off the rest of the paster processes (they usually don't get stopped if the main running process is killed).

The script is pretty rough and expects the production.ini to be in your package's main folder, with the development.ini being in the same directory as the setup.py (one directory above the production.ini). Make sure you change my_paster_package to be whatever your project is called, like "movies" from the turbogears example

Of course if someone has a better way of doing this that would be great too! (wsgi isn't an option for me, and it seems difficult to set it up when your project is installed as an egg)