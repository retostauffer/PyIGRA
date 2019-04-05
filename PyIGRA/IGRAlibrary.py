# -------------------------------------------------------------------
# - NAME:        IGRAread.py
# - AUTHOR:      Reto Stauffer
# - DATE:        2016-10-11
# -------------------------------------------------------------------
# - DESCRIPTION: Extracting IGRA data sets.
# -------------------------------------------------------------------
# - EDITORIAL:   2016-10-11, RS: Created file on thinkreto.
# -------------------------------------------------------------------
# - L@ST MODIFIED: 2019-04-05 09:07 on marvin
# -------------------------------------------------------------------


# -------------------------------------------------------------------
# Initialize logger
# -------------------------------------------------------------------
import logging, logging.config
log = logging.getLogger("PyIGRA.lib")

# -------------------------------------------------------------------
# RASO class to store the data
# -------------------------------------------------------------------
class raso( object ):

   # Initialization routine. Input 'header' has to be a tuple
   # containing the necessary header information in a specific order
   # as read.
   def __init__(self, header):
      """raso(header)

      Helper class ``raso'' (radio sounding) which stores the the 
      observation blocks. Each sounding is represented by a block.

      Parameters
      ----------
      header : list
         header line extracted from the IGRA data file.
         The header contains information about date, time,
         station, ...
      """

      # Convert date/time elements
      self.NOMINAL = {}
      self.NOMINAL["yyyy"] = int(header[1])
      self.NOMINAL["mm"]   = int(header[2])
      self.NOMINAL["dd"]   = int(header[3])
      self.NOMINAL["HH"]   = int(header[4])
      self.RELEASE = {}
      self.RELEASE["HH"]   = int(header[5][0:2])
      self.RELEASE["MM"]   = int(header[5][2:])

      self.LEVELS    = int(header[6])
      self.P_SRC     = str(header[7])
      self.NP_SRC    = str(header[8])
      self.LAT       = float(header[9]) / 1.e4 
      self.LON       = float(header[10]) / 1.e4
      self.DATA      = []   # No data: empty list


   # Small print method for raso objects
   def show(self, parameters, paramconfig, head = True, fid = None):
      """show(parameters, paramconfig, head = True, fid = None)

      Method to create output (either to stdout or write the data
      into a file, see fid).
      Loops trough the extracted data and prints the observations.

      Parameters
      ----------
      parameters : list
         list of strings, names of the parameters to be shown.
      paramconfig : dictionary
         The parameter config as returned by returned by PyIGRA.Config.
         Keys: parameter name; values: dict object
         with (at the moment) a format specification. E.g.,
         {'TEMPERATURE':{'format':'{:7.2f}'},...}
      head : boolean
         default is True, whether or not the header should be printed.
      fid: either None or a file handler
         If None the output will be
         printed on stdout. If a file handler the data will be written
         into the file specified by the file handler rather than printed
         to stdout.

      Returns
      -------
      No return, outputs data to stdout or file.
      """

      # Looping trough data (levels) and prints data
      for i in range(0,len(self.DATA)):
         # Print header
         if head and i==0:
            if fid:
               fid.write("NOMINAL    RELEASE {0:s}\n".format(" ".join(parameters)))
            else:
               print("{0:s} {1:s}".format("NOMINAL", " ".join(parameters)))
         # Print time stamp
         NOMINAL = "{0:04d}{1:02d}{2:02d}{3:02d}".format(self.NOMINAL["yyyy"],
                    self.NOMINAL["mm"],self.NOMINAL["dd"],self.NOMINAL["HH"])
         RELEASE = "{0:02d}{1:02d}".format(self.RELEASE["HH"],self.RELEASE["MM"])
         # Show data
         self.DATA[i].show(NOMINAL, RELEASE, parameters, paramconfig, fid)

   # Method to append data. Given format. Input is tuple from
   # regex match (re.match) in a certain order!
   def append(self,data):
      """append(data)

      Helper function appending observations to the raso objects.
      Given input "data" a new raso_data object is created and appendet
      to self.DATA.

      Parameters
      ----------
      data : list
         containing one observation (one line) from the IGRA data file.

      Returns
      -------
      No return.
      """
      self.DATA.append(raso_data(data))

   # Check if we have as much data stored as indicated by the header
   def checklevels(self):
      """checklevels()

      The header contains number of expected levels/observations
      per block. Checking levels. If less lines of data have been
      extracted than number levels expected the script will run into
      an error. Note: entries exists where more data than the number
      of expected levels will be returned wherefore the if condition
      is set to "len(self.DATA) < self.LEVELS".
      """
      #if not len(self.DATA) == self.LEVELS:
      if len(self.DATA) < self.LEVELS:
         log.error("only {0:d}/{1:d} data lines loaded. Stop.".format(len(self.DATA),self.LEVELS))
         import sys; sys.exit(9)


# -------------------------------------------------------------------
# Raso data class
# -------------------------------------------------------------------
class raso_data(object):

   def __init__(self,data):
      """raso_data(data)

      Helper class raso_data. Each data IGRA data line consists of a set
      of observed values (can be missing as well) such as TEMPERATURE,
      GPHEIGHT, DEWPOINT, ...
      This object parses and stores these values.

      Parameters
      ----------
      data : list
         containing one observation (one line) from the IGRA data file.

      Returns
      -------
      Returns nothing, stores input data on the object itself.
      """

      # Data/code description see:
      # - http://www1.ncdc.noaa.gov/pub/data/igra/data/igra2-data-format.txt
      self.TYP1             = int(data[0])
      self.TYP2             = int(data[1])
      self.PRESSURE_FLAG    = "-" if data[4] == " " else data[4]
      self.GPHEIGHT_FLAG    = "-" if data[6] == " " else data[6]
      self.TEMPERATURE_FLAG = "-" if data[8] == " " else data[8]
      self.ELAPSEDTIME      = int(data[2])    if int(data[2])  <= -8888 else int(data[2][0:3])*60+int(data[3:])
      self.PRESSURE         = float(data[3])  if int(data[3])  <= -9999 else float(data[3])/1.e2
      self.GPHEIGHT         = float(data[5])  if int(data[5])  <= -9999 else float(data[5])
      self.TEMPERATURE      = float(data[7])  if int(data[7])  <= -8888 else float(data[7])/10.
      self.RELHUMIDITY      = float(data[9])  if int(data[9])  <= -8888 else float(data[9])/10.
      self.DEWPOINT         = float(data[10]) if int(data[10]) <= -8888 else float(data[10])/10.
      self.WINDDIRECTION    = int(data[11])   if int(data[11]) <= -8888 else int(data[11])
      self.WINDSPEED        = float(data[12]) if int(data[12]) <= -8888 else float(data[12])/10.

   # Print data
   def show(self, NOMINAL, RELEASE, parameters, paramconfig, fid):
      """show(self, NOMINAL, RELEASE, parameters, paramconfig, fid)

      Helper method to show/display the data.

      Parameters
      ----------
      NOMINAL : string
         nomal date/time of the sounding (format YYYYmmddHH)
      RELEASE : string, release time (HHMM; often "9999")
      parameters : list
         object of characters to specify what should be
         printed (e.g., ['TEMPERATURE','PRESSURE']
      paramconfig : dictionary
         The parameter config as returned by returned by PyIGRA.Config.
         Keys: parameter name; values: dict object
         with (at the moment) a format specification. E.g.,
         {'TEMPERATURE':{'format':'{:7.2f}'},...}
      fid: either None or a file handler
         If None the output will be
         printed on stdout. If a file handler the data will be written
         into the file specified by the file handler rather than printed
         to stdout.

      Returns
      -------
      No return. Either prints the data on stdout or writes it to a
      file (see in put fid).
      """

      tmpdata = [NOMINAL, RELEASE]
      for rec in parameters: tmpdata.append(getattr(self, rec)) #"self.{0:s}".format(rec))
      tmpfmt  = ["{:s}", "{:s}"]
      for rec in parameters: tmpfmt.append(paramconfig[rec]['format'])
      tmpfmt  = " ".join(tmpfmt)

      if fid:
         #eval("fid.write(\'{0:s}\\n\' % tuple(({1:s})))".format(" ".join(tmpfmt),",".join(tmpdata))) 
         tmpfmt += "\n"
         fid.write(tmpfmt.format(*tmpdata))
      else:
         print(tmpfmt.format(*tmpdata))


