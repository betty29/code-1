## Bitmap Maker  
Originally published: 2011-04-21 12:16:15  
Last updated: 2011-04-21 13:08:46  
Author: Stephen Chappell  
  
A friend and I were discussing the possibility of creating every possible image that is 800x600x24 (800 pixels wide by 600 pixels tall and using 24-bit color). This recipe is a proof-of-concept program showing what is possible with just a 2x2 image using 15 different colors (yielding a total of 50,625 images when run). In terms of the original thought experiment, a total of `16777216 ** 480000` images should be possible given the 800x600x24 specifications (or `1 << 11520000` in binary). In base 10 that is `10 ** 3467865.55` and shows that there are an enormous number of possible states that a 800x600 canvas can take.

If you have any comments or wish to down-vote this recipe, please provide your insight as to what could be improved upon and how you would go about fixing any problems that you might find.