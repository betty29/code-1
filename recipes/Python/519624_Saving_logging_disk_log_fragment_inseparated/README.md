## Saving [logging.] disk log fragment into separated file  
Originally published: 2007-05-08 07:26:44  
Last updated: 2007-05-08 07:26:44  
Author: Denis Barmenkov  
  
Sometime I want extract part of disk-based log file, created by standard
logging module) into separated file on disk.
This recipe shows simple technique to acquire this.

Sample: processing tasks in loop, so on exit I have few logs: on log per task.