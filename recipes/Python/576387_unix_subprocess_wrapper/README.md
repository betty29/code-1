## unix subprocess wrapper  
Originally published: 2008-07-29 07:09:46  
Last updated: 2008-07-29 07:11:17  
Author: Pádraig Brady  
  
I have used this for ages to control child processes (and all their children). Some of the existing subprocess module was based on this, but I find this simpler for my uses at least.

# Example:
    import subProcess
    process = subProcess.subProcess("your shell command")
    process.read() #timeout is optional
    handle(process.outdata, process.errdata)
    del(process)