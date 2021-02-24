## edit dictionary values (possibly restrained) with Tkinter  
Originally published: 2011-03-15 21:37:53  
Last updated: 2011-03-15 21:37:54  
Author: s_h_a_i_o   
  
The behaviour of applications sometimes depends on various parameters that can be chosen by the user through some GUI. Quite often, these parameters need take value in a predefined set. Parameters include for instance:
- The number of replications for a simulator.
- Dates of beginning/end of sample for time series access/plot.
- Log writing

This recipe assumes that
* Such parameters are stored in a dictionary. Values in the dictionnary are used as initial values for the parameters.
* Values are "singleton", i.e non iterable (although they may be strings).
* When a value is a list instance, its content represent the set of possible values 
The recipe offers a simple way to edit the values in a Tkinter Frame, by adding proper widget to it (constrained value are menubutton while unconstrained values are edit widgets).

This is done by the function apply(frame,dict,position), which adds to the Tkinter frame the necessary widgets to edit the dictionary dict. Widgets are placed using grid (hence the frame needs use grid() too) and span on two columns. topleft position (x,y) in grid is specified using position= (x,y,0,0)



