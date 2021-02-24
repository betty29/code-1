## Functional imaging  
Originally published: 2002-06-17 15:00:37  
Last updated: 2002-06-17 15:00:37  
Author: andreas kupries  
  
Origin: http://wiki.tcl.tk/3523
Author: Richard Suchenwirth

Cameron Laird pointed me to Conal Elliott's Pan project ("Functional Image Synthesis", [http://research.microsoft.com/~conal/papers/bridges2001/]), where images (of arbitrary size and resolution) are produced and manipulated in an elegant functional way. Functions written in Haskell (see Playing Haskell) are applied, mostly in functional composition, to pixels to return their color value. FAQ: "Can we have that in Tcl too?"
As the funimj demo below shows, in principle yes; but it takes some patience (or a very fast CPU) - for a 200x200 image the function is called 40000 times, which takes 9..48 seconds on my P200 box. Still, the output often is worth waiting for... and the time used to write this code was negligible, as the Haskell original could with few modifications be represented in Tcl. Functional composition had to be rewritten to Tcl's Polish notation - Haskell's

 foo 1 o bar 2 o grill

(where "o" is the composition operator) would in Tcl look like
 o {foo 1} {bar 2} grill

As the example shows, additional arguments can be specified; only the last argument is passed through the generated "function nest":
 proc f {x} {foo 1 [bar 2 [grill $x]]}

But the name of the generated function is much nicer than "f": namely, the complete call to "o" is used, so the example proc has the name
 "o {foo 1} {bar 2} grill"

which is pretty self-documenting ;-)