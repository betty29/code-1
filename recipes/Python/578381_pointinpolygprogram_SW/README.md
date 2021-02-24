## A point-in-polygon program (S.W. Sloan algorithm)  
Originally published: 2012-12-16 12:09:35  
Last updated: 2014-04-24 18:13:34  
Author: PG   
  
Class to compute if a point(s) lies inside/outside/on-side of a polygon.

UPDATE: The class now works with sequences of points.


This is a Python 3 implementation of the Sloan's improved version (FORTRAN 77 code) of the Nordbeck and Rystedt algorithm, published in the paper:

SLOAN, S.W. (1985): A point-in-polygon program. Adv. Eng. Software, Vol 7, No. 1, pp 45-47.

This class has 1 public method (is_inside) that returns the minimum distance to the nearest point of the polygon:

If is_inside < 0 then point is outside the polygon.
If is_inside = 0 then point in on a side of the polygon.
If is_inside > 0 then point is inside the polygon.