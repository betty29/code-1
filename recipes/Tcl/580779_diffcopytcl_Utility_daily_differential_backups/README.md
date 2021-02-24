## diff_copy.tcl Utility for daily differential backups of large windows directory structures  
Originally published: 2017-04-10 13:51:57  
Last updated: 2017-04-10 13:51:58  
Author: John Brearley  
  
When you have terrabytes of data with 100,000+ files, it is no longer practical to blindly copy the entire data structure on a daily basis. I wrote this utility diff_copy.tcl to sort out what has been changed/updated and what new files have been added and only copy the changed & new items. If the date/time of the source file is newer, the file will be copied. If the date/time of the source file is the same as the destination, the file sizes in bytes are checked to decide if a copy is necessary. If the source file is not present on the destination directory, the file is copied. There are options to remove old files from the destination directory or show what would be copied, but not actually do the copy.