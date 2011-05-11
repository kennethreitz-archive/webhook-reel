webhook-reel
============

Jenkins doesn't let you trigger builds via webhook POSTs.

This will work.




Routes
------

``/``
    Text box for entering request type and URL.
    Returns webook-reel url, w/ clippy.

``/get/<url>``
    GETs given url.

``/head/<url>``
    HEADs given url.

``/put/<url>``
   PUTs given url.

``/post/<url>``
    I have no idea why you'd want to do this.



Future
------

- Support for optional data and paramaters
- Templating for inserting webhook data (jinja2)


License
-------

ISC.

