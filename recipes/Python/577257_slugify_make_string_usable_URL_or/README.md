## slugify: make a string usable in a URL or filename  
Originally published: 2010-06-07 03:58:37  
Last updated: 2010-06-07 04:11:55  
Author: Trent Mick  
  
"Slugify" a string so it is ascii, has only alphanumeric and hyphen characters. Useful for URLs and filenames. This is heavily based on the slugify in Django.

Note: presumes that you've `import re`d higher up in your module.