"""
setup.py for FLiP, just metadata.  To create the FLiP 1.0 page at PyPI:

 python setup.py register

see http://docs.python.org/distutils/packageindex.html

This setup.py names no packages. It is not intended to support sdist, install...
"""

from distutils.core import setup

setup(
    # Metadata for PyPI
    # from http://docs.python.org/distutils/setupscript.html#meta-data
    # also http://docs.python.org/distutils/apiref.html#module-distutils.core
    name = 'FLiP',
    version = '1.0',
    author = 'Jonathan Jacky',
    author_email = 'jon@u.washington.edu',
    maintainer = 'Jonathan Jacky',
    maintainer_email = 'jon@u.washington.edu',
    url = 'http://staff.washington.edu/jon/flip/www/',
    description = 'F L i P : Logical Framework in Python',
    long_description = open('README.rst').read(),
    download_url = 'http://staff.washington.edu/jon/flip/www/download.html',
    license = 'GNU General Public License (GPL)',

    keywords = 'logical framework python theorem prover proof checker natural deduction',

    # from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.3',
        'Topic :: Scientific/Engineering :: Mathematics',
        ],

    # support python setup.py sdist
    packages = [ 'flip',  'flip.test', 'witch' ],
)
