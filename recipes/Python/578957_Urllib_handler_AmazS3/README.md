## Urllib handler for Amazon S3 buckets  
Originally published: 2014-11-06 18:31:44  
Last updated: 2014-11-06 18:31:44  
Author: Andrea Corbellini  
  
This is a handler for the standard [urllib.request](https://docs.python.org/dev/library/urllib.request.html) module capable of opening buckets stored on [Amazon S3](http://aws.amazon.com/s3/).

Here is an usage example:

    >>> from urllib.request import build_opener
    >>> opener = build_opener(S3Handler)
    >>> response = opener.open('s3://bucket-name/key-name')
    >>> response.read()
    b'contents'