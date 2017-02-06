#!/bin/bash
# -------------------------------------------------------------------
# PyIGRA test script (bash shell)
# -------------------------------------------------------------------


# Searching for a station, in this case Innsbruck
venv/bin/PyIGRA_search --id inns

# Should print "AUM00011120  47.2603   11.3439  581.0    INNSBRUCK-FLUGHAFEN ...
# Where the first part (AUM00011120) is the ID we need to download the data
venv/bin/PyIGRA --id AUM00011120 -o test1.txt
venv/bin/PyIGRA --id AUM00011120 -p PRESSURE,TEMPERATURE -o test2.txt

