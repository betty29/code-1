## Authenticating Twisted with Zope/Plone  
Originally published: 2006-02-04 08:51:00  
Last updated: 2006-02-08 00:19:44  
Author: Duncan McGreggor  
  
I was writing a custom Twisted XML-RPC server for radio station DJs to use, but one station was managing all of its internal web app users and groups through Zope. Twisted has an amazingly pluggable authentication framework, so the requirement was satisfied with the following.

Note that in this simple example, every time a user executes an XML-RPC method, they are authenticating against Zope. This involves an xmlrpclib.ServerProxy instantiation as well as the overhead of making a network connection to Zope. For this reason, as well as in the event of Zope being down, one might want to implement some form of caching (without passwords), so that application functionality is not impacted by Zope downtime and overhead from authentication is only incurred when necessary.

radix makes a very good point in the comments: the use of xmlrpclib in this recipe is blocking. This means that if you have 10, 20, whatever number of people using the app, and someone new logs in, the twisted reactor can't do it's usual thing and cycle through requests until that user finishes logging in. I will post an update that makes use of the non-blocking t.w.xmlrpc code. The solution will be messier, though, as t.w.xmlrpc is broken in that it doesn't handle scheme://username:pass@host:port URLs. This is due to the fact that t.w.xmlrpc.QueryProtocol doesn't set an Authentication header... and there's no mechanism in t.w.xmlrpc.Proxy and QueryFactory for parsing and setting user and password into from the URL.

Update: see the comments below for how to work around this limitation.