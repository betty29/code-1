## Metronome For Beginner Musicians...  
Originally published: 2012-05-18 19:26:29  
Last updated: 2012-05-18 19:30:04  
Author: Barry Walker  
  
This DEMO code is a simple metronome for the Linux platform. It is for newcomers to playing musical instruments as a timing unit for practicing with.

It is issued as Public Domain and you may do with it as you please...

The device /dev/dsp IS required for this to work. If your machine lacks this then install oss-compat from you distro's repository.

It exploits a flaw in the default /dev/dsp device inside linux...

The part of the code the uses Ctrl-C to exit a loop has a flaw. This is not a bug. I will let the big guns explain what is happening if they want to in the comments section.

Enjoy finding simple solutions to often very difficult pronblems...

Bazza, G0LCU...
