## Random user generator  
Originally published: 2012-02-27 16:45:42  
Last updated: 2012-02-27 16:58:33  
Author: Koppula Varun Raj  
  
I've worked on a random user generator in C a long time ago, so I thought I'd make an advanced version of it in Python(3.2). I'll have you know, I am an amateur in Python and even programming for that matter so I'd really appreciate some criticism on my code and what more can be added.

About the program - I've added a default list of users, you can modify the list to your convenience and for data persistence, I made use of the pickle module. The random module plays the pivotal role generating the output making use of the choice method. Those along with the os module if the program is being run for the first time on a pc, it will create a data file with the default list.After some digging around, I managed to find os.getlogin() from the python library which was exactly what I was looking for (to get the computer's name making sure it can get the data file to the correct directory). I'm a little skeptical about that part, wondering whether or not it will work on every pc.