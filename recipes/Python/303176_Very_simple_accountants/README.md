## *Very* simple accountant's calculator  
Originally published: 2004-09-02 10:54:01  
Last updated: 2004-09-02 10:54:01  
Author: Brett Cannon  
  
One of the signs that you love Python is when you start to use it as a simple calculator.  The problem with that is beyond the usefulness of 'sum' the interactive interpreter is not optimal for any calculations beyond a few numbers.  This mostly seems to stem from the numbers not being formatted in a nice fashion; ``2345634+2894756-2345823`` is not the easiest thing to read.  That's where an accountant's calculator comes in handy; the tape presents numbers in a column view that is very uncluttered.  And thanks to the decimal package a *very* simple one can be implemented quickly.

To use this recipe you input the number, an optional space, and then the operator (/, *, -, or +; everything you would find on the numeric keypad on your keyboard) and then press return.  This will apply the number to the running total using the operator.  To output the total just enter a blank line.  To quit enter the letter 'q' and press return.  This simple interface matches the output of a typical accountant's calculator, removing the need to have some other form of output.