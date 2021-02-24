## HTML Page Scraping (of the Quick and Dirty Variety)  
Originally published: 2003-12-31 09:34:48  
Last updated: 2003-12-31 17:43:07  
Author: Bill Bell  
  
This recipe is really about using previously identified information in a web page--ie, state information--to decide how to use newly identified information. To view a page of the kind that can be scraped using the code below visit
http://www.archives.ca/02/02012202_e.html
select "Ontario", enter "Cornwall" in the Geographic Location box, and select "MAX" in the Number of References per page list.

Two kinds of document images are offered within each page served by the census site, namely, schedule 1 document images and schedule 2. Only the schedule 1
documents provide information in which I have an interest at present (namely surnames, birthdates, etc). I would, therefore, like to extract information that identifies schedule 1 images and ignore the others.

Put in terms of state, when my script notices that it has most recently seen HTML code indicating schedule 1 I want it to extract information in the URLs in the "option" tags; when it has found schedule 2 I want it to ignore the URLs. It might be that one of the simplest ways of doing this is to form a regular expression (RE) that alternates one RE that recognises schedule numbers and one RE that recognises the URLs, then use this whole RE with a "sub" function so that the matches can be processed in a purpose-built function.

Incidentally, I have found that Phil Schwartz' "Kodos" Python Regex Debugger makes it a lot faster to create and check REs. Many thanks, Phil!