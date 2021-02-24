## Monitor Progress of File Descriptors of Another Process  
Originally published: 2014-05-19 11:16:47  
Last updated: 2014-05-30 01:10:53  
Author: Alfe   
  
This tool (inspired by azat@stackoverflow, see http://stackoverflow.com/a/16082562/1281485) allows to watch the progress of the file descriptors of another process.  This can be used, for example, if you transfer a file to another host and the transferring program does not show any progress indication itself.  Instead of waiting blindly until the routine is done, with this tool you can use Linux's proc file system to monitor the progress of the other process while it walks through the file.

The tool continuously monitors the position in and the size of the files the given process's file descriptors point to.  For growing (or shrinking, but that's very unusual) files, a time when it was (or will be) empty is computed ("emptyTime"), for moving file descriptors (the typical case), the time when it started at position 0 ("startTime"), the time when it will reach the current size of the file ("reachTime") and when it will meet with the end of a growing (or shrinking) file is computed ("meetTime").

For fixed-size files the meetTime will be the same as the reachTime of course.  The meetTime only makes sense in case a file is growing and at the same time read (e. g. when a movie is downloaded to a file by one process and converted by a different process; using this tool can tell you when the converter process might run dry on the input because the download wasn't fast enough, and in this case you maybe can pause the converter to prevent this situation).

The tool is designed as a library; the display of the information is independent from the gathering of the data.  Please feel free to create more fancy displays, add percentage output etc.