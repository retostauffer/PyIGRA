# -------------------------------------------------------------------
# - NAME:        setup.py
# - AUTHOR:      Reto Stauffer
# - DATE:        2019-04-05
# - LICENSE: GPL-2, Reto Stauffer
# -------------------------------------------------------------------
# - DESCRIPTION: A small package which allows to download and extract
#                data from the integrated global radiosonde archive
#                version 2 (IGRA2). 
# -------------------------------------------------------------------
# - L@ST MODIFIED: 2019-04-05 10:35 on marvin
# -------------------------------------------------------------------
from setuptools import setup

setup(name             = "PyIGRA", # This is the package name
      version          = "0.2.post0",  # Current package version, what else
      description      = "Downloading and extracting data from the integrated global radiosonde archive",
      long_description = "No long description necessary",
      classifiers=[
        "Development Status :: 4 - Beta",
        "GNU Lesser General Public License v2 (GPL-2)",
      ],
      keywords     = "raso sounding IGRA",
      url          = "https://bitbucket.org/retos/pyimgibufr",
      author       = "Reto Stauffer",
      author_email = "reto.stauffer@uibk.ac.at",
      license              = "GPL-2",
      packages             = ["PyIGRA"],
      install_requires     = ["ConfigParser"],
      scripts              = ["bin/PyIGRA","bin/PyIGRA_search"],
      include_package_data = True,
      zip_safe = False)


