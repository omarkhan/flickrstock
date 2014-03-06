#!/usr/bin/env python

from itertools import islice
from urllib import urlretrieve
import os.path
import re

from flickrapi import FlickrAPI


# Creative commons licence ids
LICENCES = (4, 5, 6, 7)


def slugify(value):
    """
    From django: converts to lowercase, removes non-alpha characters, and
    converts spaces to hyphens.
    """
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return re.sub('[-\s]+', '-', value)


class Downloader(FlickrAPI):
    def fetch(self, *tags, **kwargs):
        if not tags:
            raise ValueError('Specify some tags to search for')

        # Default options
        size = kwargs.setdefault('size', 'c')
        output = kwargs.setdefault('output', slugify('-'.join(tags)))
        limit = kwargs.setdefault('limit', 10)
        url_field = 'url_%s' % size.lower()

        # Arguments for the flickr api
        options = {
            'tags': ','.join(tags),
            'tag_mode': 'all',
            'license': ','.join(map(str, LICENCES)),
            'content_type': '1',  # no screenshots
            'media': 'photos',    # no videos
            'extras': url_field,
        }
        photos = self.walk(**options)

        # Make the output dir, fail if it already exists
        os.mkdir(output)

        for photo in islice(photos, 0, limit):
            url = photo.attrib[url_field]
            filename = os.path.basename(url)
            urlretrieve(url, os.path.join(output, filename))
            yield url


if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser(description='Fetch public photos from flickr')
    parser.add_argument('tag', nargs='+', help='tags to search for')
    parser.add_argument('-s', '--size', choices=('sq', 't', 's', 'q', 'm', 'n',
                                                 'z', 'c', 'l', 'o'),
                        default='c', help='photo size')
    parser.add_argument('-l', '--limit', type=int, default=10, help='how many photos')
    parser.add_argument('-k', '--key', help='flickr api key')
    parser.add_argument('-o', '--output', help='output directory')
    args = vars(parser.parse_args())
    tags = args.pop('tag')
    api_key = args.get('key') or os.environ['FLICKR_API_KEY']

    flickr = Downloader(api_key)
    for url in flickr.fetch(*tags, **args):
        print(url)
