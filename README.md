

Currently testing against python 2.7, python 3.4, 3.5, and 3.6
(see [travis config](.travis.yml)).
[![Build Status](https://travis-ci.org/retostauffer/PyIGRA.svg?branch=master)](https://travis-ci.org/retostauffer/PyIGRA)

# The PyIGRA Package

The [National Centres for Environmental Information](https://www.ncdc.noaa.gov/data-access/weather-balloon/integrated-global-radiosonde-archive)
provides a large global archive for vertical soundings also known as radiosondes.
__PyIGRA__ downloads and extracts data from the
[Integrated Global Radiosonde Archive](https://www.ncdc.noaa.gov/data-access/weather-balloon/integrated-global-radiosonde-archive)
data set and prepares them in a more handy data format.

**NOTE (2017)**: Slightly changed output format. The data set provides information
about the nominal time (date/time when the sounding was planned) and
a release time (actual release time). In an earlier version I've tried
to combine them in a simple way which was not always correct. I've decided
to return the full information.

* `NOMINAL`: nominal date/hour of the sounding (format `yyyymmddHH`).
    `HH` _can be 99 (missing)_.
* `RELEASE`: release time, format is `HHMM` (hour/minute).
    Can be `0000` trough `2359`. If minute is missing the last two
    digits are `99`. If both, hour and minute is missing, a `9999`
    is returned.

For more details please read the data set [format description file](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt).


# Package Installation

Clone git repository and install the package via:

```bash
   git clone https://github.com/retostauffer/PyIGRA.git PyIGRA
   python setup.py install
```

Or directly install via github:

```bash
   pip install git+https://github.com/retostauffer/PyIGRA.git
```

You may use `sudo python ...` or `sudo pip install ...` depending on your
system.  Requires the additional python module `ConfigParser`.


# Using the PyIGRA Package

There is a script called **PyIGRA_test.sh** which provides an
example of the main functionality of the PyIGRA package

```bash
   # Searching for a station, in this case Innsbruck
   PyIGRA_search --id inns

   # Should print "AUM00011120  47.2603   11.3439  581.0    INNSBRUCK-FLUGHAFEN ...
   # Where the first part (AUM00011120) is the ID we need to download the data
   PyIGRA --id AUM00011120 -o test1.txt
   PyIGRA --id AUM00011120 -p PRESSURE,TEMPERATURE -o test2.txt

   # Additional arguments:
   # For testing/development: only print the first 2 entries
   PyIGRA --id AUM00011120 -l 2

   # Keep zip file after download. If PyIGRA is called again (and the
   # zip file exists on disc) no download will be required.
   PyIGRA --id AUM00011120 --keep

   # Change output format (only extract TEMPERATURE and PRESSURE
   PyIGRA --id AUM00011120 --parameters TEMPERATURE,PRESSURE
```

PyIGRA_seach is reading the latest station list and can be used to get the
proper station identifier (-i/--id) needed for the PyIGRA executable.
PyIGRA is downloading a zip file from the ftp server, extracts the data,
and outputs the data in a new format. In this case the data will be
piped into the output file (-o/--output) as specified in the script.


# INFORMATION

- Autor:    Reto Stauffer<at>uibk.ac.at
- Date:     2019-04-05
- License:  GPL-2

A detailed description of the IGRA2 data format:
- [ftp://ftp.ncdc.noaa.gov/pub/data/igra/igra2-list-format.txt](ftp://ftp.ncdc.noaa.gov/pub/data/igra/igra2-list-format.txt) (station list format)
- [ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt](ftp://ftp.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt) (data format)

Station list used by PyIGRA_search:
- [http://www1.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt](http://www1.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt)

Direct data access:
- [http://www1.ncdc.noaa.gov/pub/data/igra/data/data-por/](http://www1.ncdc.noaa.gov/pub/data/igra/data/data-por/)


