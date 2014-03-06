from distutils.core import setup

setup(
    name='flickrstock',
    version='0.1',
    description='Download stock photos from flickr',
    author='Omar Khan',
    author_email='omar@omarkhan.me',
    url='https://github.com/omarkhan/flickrstock',
    py_modules=['flickrstock'],
    scripts=['flickrstock'],
    requires=['flickrapi'],
)
