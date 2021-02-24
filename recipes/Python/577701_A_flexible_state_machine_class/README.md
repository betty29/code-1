## A flexible state machine class  
Originally published: 2011-05-18 14:26:59  
Last updated: 2011-05-18 15:17:02  
Author: Mike Sweeney  
  
The operation of the state machine is defined by transitions. The transitions
control what value is returned and which new state to switch to, given an
"event" input when in a certain current "state". State machines have many
applications such as games, process controls, and language parsing.