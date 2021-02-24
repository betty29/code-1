## Run asynchronous tasks using coroutines  
Originally published: 2010-03-19 10:11:16  
Last updated: 2010-08-06 16:16:20  
Author: Arnau Sanchez  
  
This recipe shows a simple, transparent (and hopefully pythonic) way of running asynchronous tasks when writing a event-driven application (i.e. GUI). The aim is to allow a programmer to write time-consuming functions (usually IO-bound, but not only) with sequential-looking code, instead of scattering the logic over a bunch of callbacks. We will take advantage of the coroutines introduced in Python 2.5 (see http://www.python.org/dev/peps/pep-0342). 

The goal: wouldn't it be great if we could write something like this?

    def myjob(entry, arg1, arg2, arg3):
        result1 = function_that_takes_eons_to_complete(arg1, arg2)    
        result2 = another_function_that_downloads_a_big_really_big_file(result1, arg3)
        entry.set_text("The result is: %d" % result2)
    
    def on_start_button___clicked(button, entry):
        myjob(entry, 1, 2, 3)
        
    ...    
    gtk.main()

Indeed, but we can't! The GUI will hang until the job is done and the user will be rightfully angry. Coroutines to the rescue: the absolute minimal change we can make to this code is transforming *myjob* into a coroutine and yield every time we do blocking stuff:

    def myjob(entry, arg1, arg2, arg3):
        result1 = yield some_task(arg1, arg2)    
        result2 = yield some_other_task(result1, arg3)
        entry.set_text("The result is: %d" % result2)
    
    def on_start__clicked(button, entry):
        start_job(myjob(entry, 1, 2, 3))
                    
*some_task* and *some_other_task* are here the asynchronous implementation of the sequential tasks used in the first fragment, and *start_job* the wrapper around the coroutine. Note that we still have to implement non-blocking versions of the tasks, but they are usually pretty generic (wait some time, download a file, ...) and can be re-used. If you happen to have a CPU-bound function or even a IO-bound code you cannot split (*urllib2* anyone?), you can always use a generic threaded task (granted, the whole point of using co-routines should be avoiding threads, but there is no alternative here).

At the end, all the plumbing we need to make it work is just 1 function: *start_job* (wrapper around the job to manage the flow of the coroutine). The rest of the code -two asynchronous tasks (*sleep_task*, *threaded_task*) and a demo app- are shown solely as an example.