## Credit Card Validation  
Originally published: 2011-08-11 19:06:57  
Last updated: 2011-08-11 19:06:58  
Author: Stijn de Graaf  
  
Test validity of any credit card number using the LUHN method (mod 10).
Starting at the last digit and moving backwards, you add up every other digit.
Then, you double the left-out digits, and add the digits of these results to the original sum.
If this satisfies       sum mod 10 == 0    then the card is valid.

This is also explained at http://www.beachnet.com/~hstiles/cardtype.html