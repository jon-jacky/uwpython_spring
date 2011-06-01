"""
setup.py for FLiP, Logical Framework in Python
see http://docs.python.org/distutils/packageindex.html

To create or update the FLiP page at PyPI: python setup.py register
To make distribution: python setup.py sdist -v -f --formats=gztar,zip
It is possible to use FliP from the unpacked distribution without install
To install from the unpacked distribution: python setup.py install
"""

from distutils.core import setup

setup(
    # Metadata for PyPI
    # To create the FLiP 1.0 page at PyPI: python setup.py register
    # see http://docs.python.org/distutils/setupscript.html#meta-data
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
        'Operating System :: OS Independent',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.3',
        'Topic :: Scientific/Engineering :: Mathematics',
        ],

    # Packages and other files to include in distribution
    # To make distribution: python setup.py sdist -v -f --formats=gztar,zip
    packages = [ 'flip',  'flip.test', 'witch' ],
    package_data = { 'flip.test' : [ '*.ref' ],  # expected test output
                     'witch' : [ '*.txt', 'cpath', 'cpath.bat' ] },
    data_files = [ ('notes', [ '*.txt' ]),
                   ('www', [ '*.html' ]) ]
    
    )
