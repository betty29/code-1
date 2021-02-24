## Yet another reinvention of a Python HTML generation mechanism  
Originally published: 2005-09-16 00:14:45  
Last updated: 2005-11-22 07:25:44  
Author: Josiah Carlson  
  
The other day I was complaining about writing html, forms, etc., for Python cgi and/or web programming.  I had pointed out a selection of three examples, the first of which ended up being very much like Nevow.stan .  Thinking a bit about it, I realized that stan had issues in that you couldn't really re-use pre-defined tags with attributes via map, and keyword arguments were just too darn convenient to swap the calling and getitem syntax.

Instead, I hacked together a mechanism that supports:
T.tagname("content", T.tagname(...), ..., attr1='value', ...)
T.tagname(attr1='value', ...)("content", T.tagname(...), ...)
x = T.tagname(attr1='value', ...)
y = T.tagname(*map(x, ['content', ...]))
... and many other options.

Essentially, you can mix and match calls as much as you want, with three memory and sanity saving semantics:
1. Creating a new tag object via T.tagname, or any call of such, will create a shallow copy of the object you are accessing.
2. smallred = T.font(size='-1', color='red');bigred = smallred(size='+1') Works exactly the way you expect it to.  If it doesn't work the way you expect it to, then your expectations are confused.
3. If you are adding content that sites within the tag, the content is replaced, not updated, like attributes.

This simple version handles auto-indentation of content as necessary (or desireable), auto-escaping of text elements, and includes an (I believe) nearly complete listing of entities which don't require closing tags.

I don't know where this is going, whether it can or will expand into something more, or what, but I believe what I have managed to hack together is better than other similar packages available elsewhere (including this recipe over here http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/366000 , which I discovered after writing my own).  Funny how these things work out.  Astute observers will note that I borrow nevow.stan's meme of using T.tagname for generating tag objects.