## farey: Numeric to rational via Farey fractions  
Originally published: 2001-04-02 20:09:38  
Last updated: 2001-04-02 20:09:38  
Author: Scott David Daniels  
  
This converts a Numeric to a rational.  The result is always
in reduced form, but the proof, while possible, is subtle.

farey(math.pi,100) = (22,7)