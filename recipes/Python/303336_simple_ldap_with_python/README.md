## simple ldap with python  
Originally published: 2004-09-03 09:35:09  
Last updated: 2004-09-03 09:35:09  
Author: John Nielsen  
  
The ldap library at http://python-ldap.sourceforge.net wraps the Openldap C api.
It can talk to various versions of ldap servers not just the Openldap servers.
Note the use of the '_s' methods like search_s which all are synchronous.
Here are some simple examples showing one how to use the library.