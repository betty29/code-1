## Implementing function-based callbacks in Python  
Originally published: 2017-04-19 17:58:24  
Last updated: 2017-04-19 18:03:11  
Author: Vasudev Ram  
  
This recipe shows a simple way of implementing callbacks in Python. There are a few ways this can be done. The way shown here uses a simple function-based approach.

In a nutshell, a callback can be informally described like this: function **a** calls function **b**, and wants to make **b** run a specific independent chunk of code at some point during **b**'s execution. We want to be able to vary which chunk of code gets called in different calls to **b**, so it cannot be hard-coded inside **b**. So function **a** passes another function, **c**, to **b**, as one argument, and **b** uses that parameter **c** to call the functionality that **a** wants **b** to call. (Function **b** may pass some parameters to the function represented by **c**, when it calls it. These could be either internally generated, passed from **a**, or a combination of both). So, by changing the value of the function **c** that gets passed to **b** (on different calls to **b**), **a** can change what chunk of code **b** calls.

More details and full code, description and output here:

https://jugad2.blogspot.in/2017/04/implementing-and-using-callbacks-in.html

