## A Simple Webcrawler  
Originally published: 2012-03-03 02:31:44  
Last updated: 2012-03-03 02:37:30  
Author: John   
  
This is my simple web crawler.  It takes as input a list of seed pages (web urls) and 'scrapes' each page of all its absolute path links (i.e. links in the format http://) and adds those to a dictionary.  The web crawler can take all the links found in the seed pages and then scrape those as well.  You can continue scraping as deep as you like.  You can control how "deep you go" by specifying the depth variable passed into the WebCrawler class function start_crawling(seed_pages,depth).  Think of the depth as the recursion depth (or the number of web pages deep you go before returning back up the tree).

To make this web crawler a little more interesting I added some bells and whistles.  I added the ability to pass into the WebCrawler class constructor a regular expression object.  The regular expression object is used to "filter" the links found during scraping.  For example, in the code below you will see:

cnn_url_regex = re.compile('(?<=[.]cnn)[.]com') # cnn_url_regex is a regular expression object

w = WebCrawler(cnn_url_regex)

This particular regular expression says:

1) Find the first occurence of the string '.com'

2) Then looking backwards from where '.com' was found it attempts to find '.cnn'

Why do this?

You can control where the crawler crawls.  In this case I am constraining the crawler to operate on webpages within cnn.com.

Another feature I added was the ability to parse a given page looking for specific html tags.  I chose as an example the <h1> tag.  Once a <h1> tag is found I store all the words I find in the tag in a dictionary that gets associated with the page url.

Why do this?

My thought was that if I scraped the page for text I could eventually use this data for a search engine request.  Say I searched for 'Lebron James'.  And suppose that one of the pages my crawler scraped found an article that mentions Lebron James many times.  In response to a search request I could return the link with the Lebron James article in it.

The web crawler is described in the WebCrawler class.  It has 2 functions the user should call:


1) start_crawling(seed_pages,depth)

2) print_all_page_text() # this is only used for debug purposes

The rest of WebCrawler's functions are internal functions that should not be called by the user (think private in C++).

Upon construction of a WebCrawler object, it creates a MyHTMLParser object.  The MyHTMLParser class inherits from the built-in Python class HTMLParser.  I use the MyHTMLParser object when searching for the <h1> tag.  The MyHTMLParser class creates instances of a helper class named Tag.  The tag class is used in creating a "linked list" of tags.

So to get started with WebCrawler make sure to use Python 2.7.2.  Enter the code a piece at a time into IDLE in the order displayed below.  This ensures that you import libs before you start using them.

Once you have entered all the code into IDLE, you can start crawling the 'interwebs' by entering the following:


import re

cnn_url_regex = re.compile('(?<=[.]cnn)[.]com')                


w = WebCrawler(cnn_url_regex)

w.start_crawling(['http://www.cnn.com/2012/02/24/world/americas/haiti-pm-resigns/index.html?hpt=hp_t3'],1)


Of course you can enter any page you want.  But the regular expression object is already setup to filter on cnn.com.  Remember the second parameter passed into the start_crawling function is the recursion depth.

Happy Crawling!