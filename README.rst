flickrstock
===========

Download stock photos from flickr
---------------------------------

Do you need a whole bunch of stock photos for your latest project? Or
maybe some images to flesh out a prototype? This command line tool
fetches photos with a `Creative
Commons <http://www.flickr.com/creativecommons/>`__ licence using the
flickr API.

Installation
~~~~~~~~~~~~

::

    pip install flickrstock

Usage
~~~~~

You will need a `flickr API
key <http://www.flickr.com/services/apps/create/apply>`__. It takes
about 30 seconds to get one. Set it as the ``FLICKR_API_KEY``
environment variable or pass it on the command line.

::

    usage: flickrstock [-h] [-s {sq,t,s,q,m,n,z,c,l,o}] [-n NUMBER] [-o OUTPUT]
                       [-k KEY]
                       term [term ...]

    Download stock photos from flickr

    positional arguments:
      term                  search terms

    optional arguments:
      -h, --help            show this help message and exit
      -s {sq,t,s,q,m,n,z,c,l,o}, --size {sq,t,s,q,m,n,z,c,l,o}
                            photo size
      -n NUMBER, --number NUMBER
                            how many photos
      -o OUTPUT, --output OUTPUT
                            output directory
      -k KEY, --key KEY     flickr api key

Examples
~~~~~~~~

Fetch some medium-sized pictures of pandas:

::

    $ flickrstock --size m panda

Download 5 original-size photos of hotel rooms, saving the original urls
in a separate file for attribution purposes:

::

    $ flickrstock -n 5 --size o --output ./hotel-rooms hotel room > urls.txt

Licence
~~~~~~~

MIT.
