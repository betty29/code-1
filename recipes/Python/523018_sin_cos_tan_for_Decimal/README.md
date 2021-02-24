## sin, cos, tan for Decimal  
Originally published: 2007-07-04 14:18:54  
Last updated: 2007-07-05 19:49:49  
Author: Alain Mellan  
  
Implementation of sine, cosine, tangent functions for Decimal arithmetic, using Taylor series expansion. It uses simple numerator and denominator generators.

The nice part is, the code is independent from the Decimal library. Feed it a float, it works just the same as if you feed it a Decimal (apart from the precision :-)