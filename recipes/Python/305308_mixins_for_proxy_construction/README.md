## mixins for proxy construction...  
Originally published: 2004-09-18 13:49:10  
Last updated: 2004-09-18 20:54:37  
Author: Alex Naanou  
  
Here we will demonstrate a technique that will make it possible to semi-transparently proxy an object and override/proxy methods or data including special methods like __call__.
this module will define several general tools and components that can be used as a basis for creation of various proxy classes...