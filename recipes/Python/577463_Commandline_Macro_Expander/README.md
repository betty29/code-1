## Commandline Macro Expander  
Originally published: 2010-11-15 03:20:30  
Last updated: 2010-11-15 03:27:16  
Author: Phil Rist  
  
This program is designed to be executed from a console window on a 
Win32 platform.  It expands user entered commands.  Three styles of
commands are accepted 'x comp myfile.c',  'x #!test myfile.exe test.dat'
and 'x {print} myfile.c' to extract, expand and excute commands
saved in a menu file, an arbitrary file or associated with a file
type in the Win32 registry.