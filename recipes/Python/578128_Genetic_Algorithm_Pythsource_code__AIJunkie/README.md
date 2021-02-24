## Genetic Algorithm in Python source code - AI-Junkie tutorial  
Originally published: 2012-05-12 09:57:40  
Last updated: 2012-06-19 12:59:13  
Author: David Adler  
  
A simple genetic algorithm program. I followed this tutorial to make the program http://www.ai-junkie.com/ga/intro/gat1.html.

The objective of the code is to evolve a mathematical expression which calculates a user-defined target integer.
___
KEY:

chromosome = binary list (this is translated/decoded into a protein in the format number --> operator --> number etc, any genes (chromosome is read in blocks of four) which do not conform to this are ignored.

protein = mathematical expression (this is evaluated from left to right in number + operator blocks of two)

output = output of protein (mathematical expression)

error = inverse of difference between output and target

fitness score = a fraction of sum of of total errors

_____
OTHER:

One-point crossover is used.

I have incorporated **elitism** in my code, which somewhat deviates from the tutorial but made my code more efficient (top ~7% of population are carried through to next generation)