webhook-reel
============

Jenkins doesn't let you trigger builds via webhook POSTs.

This will work.




Routes
------

``/``
    Text box for entering request type and URL.

``/get/<url>``
    GETs given url.


Future
------

``/head/<url>``
    HEADs given url.

``/put/<url>``
   PUTs given url.

``/post/<url>``
    I have no idea why you'd want to do this.

TODO
----

- Returns webook-reel url, w/ clippy.
- Support for optional data and paramaters
- Templating for inserting webhook data (jinja2)


License
-------

::

    Copyright (c) 2011 Kenneth Reitz.

    Permission to use, copy, modify, and/or distribute this software for any
    purpose with or without fee is hereby granted, provided that the above
    copyright notice and this permission notice appear in all copies.

    THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
    WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
    MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
    ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
    WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
    ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
    OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

