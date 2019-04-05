# -------------------------------------------------------------------
# - NAME:        setup.py
# - AUTHOR:      Reto Stauffer
# - DATE:        2017-02-05
# - LICENSE: GPL-3, Reto Stauffer, copyright 2014
# -------------------------------------------------------------------
# - DESCRIPTION: A small package which allows to download and extract
#                data from the integrated global radiosonde archive
#                version 2 (IGRA2). 
# -------------------------------------------------------------------
# - EDITORIAL:   2017-02-05, RS: Created file on thinkreto.
# -------------------------------------------------------------------
# - L@ST MODIFIED: 2019-04-05 08:35 on marvin
# -------------------------------------------------------------------
from setuptools import setup

setup(name='PyIGRA',     # This is the package name
      version='0.1-0',            # Current package version, what else
      description='Downloading and extracting data from the integrated global radiosonde archive',
      long_description='No long description necessary',
      classifiers=[
        'Development Status :: 3 - Alpha',
        #'Development Status :: 4 - Beta',
        'GNU Lesser General Public License v2 (GPL-2)',
        'Programming Language :: Python :: 2.7',
      ],
      keywords='raso sounding IGRA',
      url='https://bitbucket.org/retos/pyimgibufr',
      author='Reto Stauffer',
      author_email='reto.stauffer@uibk.ac.at',
      license='GPL-2',
      packages=['PyIGRA'],
      install_requires=['ConfigParser'],
      scripts=['bin/PyIGRA','bin/PyIGRA_search'],
      include_package_data=True,
      czip_safe=False)

