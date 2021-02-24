## Routines for programmatically authenticating with the Google Accounts system at Google App-Engine.  
Originally published: 2010-05-05 23:17:40  
Last updated: 2010-05-20 20:39:50  
Author: Berend   
  
This takes two calls, one to the ClientLogin service of Google Accounts,
and then a second to the login frontend of App Engine.

User credentials are provided to the first, which responds with a token.
Passing that token to the _ah/login GAE endpoint then gives the cookie that can
be used to make further authenticated requests.