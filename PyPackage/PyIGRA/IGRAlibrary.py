# -------------------------------------------------------------------
# - NAME:        IGRAread.py
# - AUTHOR:      Reto Stauffer
# - DATE:        2016-10-11
# -------------------------------------------------------------------
# - DESCRIPTION: Extracting IGRA data sets.
# -------------------------------------------------------------------
# - EDITORIAL:   2016-10-11, RS: Created file on thinkreto.
# -------------------------------------------------------------------
# - L@ST MODIFIED: 2017-02-06 12:47 on thinkreto
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
   def __init__(self,header):
      # Convert date/time elements
      yyyy = int(header[1]);      mm = int(header[2])
      dd   = int(header[3]);      HH = int(header[4])
      release_HH = int(header[5][0:2])
      release_MM = int(header[5][2:])
      # Append header information to object properties
      from datetime import datetime as dt
      self.ID      = header[1]
      self.DATE    = dt.strptime("%04d-%02d-%02d %02d"      % (yyyy,mm,dd,HH),                   "%Y-%m-%d %H")
      if not header[5] == "9999":
         self.RELEASE = dt.strptime("%04d-%02d-%02d %02d:%02d" % (yyyy,mm,dd,release_HH,release_MM),"%Y-%m-%d %H:%M") 
      else:
         self.RELEASE = None
      self.LEVELS  = int(header[6])
      self.P_SRC   = str(header[7])
      self.NP_SRC  = str(header[8])
      self.LAT     = float(header[9])/1.e4 
      self.LON     = float(header[10])/1.e4
      self.DATA    = []   # No data: empty list

   # Small print method for raso objects
   def show(self,parameters,paramconfig,head=True,fid=None):
      #####print "#  Raso object information:"
      #####print "#  - ID:             %s" % self.ID
      #####print "#  - Date/Hour:      %s" % self.DATE
      #####print "#  - Release:        %s" % self.RELEASE
      #####print "#  - Levels:         %d" % self.LEVELS
      #####print "#  - Position:       %.4fN %.4fS" % (self.LAT,self.LON)
      for i in range(0,len(self.DATA)):
         # Print header
         if head and i==0:
            if fid:
               fid.write("TIMESTAMP {0:s}\n".format(" ".join(parameters)))
            else:
               print "TIMESTAMP", " ".join(parameters)
         # Print time stamp
         if fid:
            fid.write("%s " % self.DATE.strftime("%s"))
         else:
            print "%s " % self.DATE.strftime("%s"),
         # Show data
         self.DATA[i].show(parameters,paramconfig,fid)

   # Method to append data. Given format. Input is tuple from
   # regex match (re.match) in a certain order!
   def append(self,data):
      self.DATA.append(raso_data(data))

   # Check if we have as much data stored as indicated by the header
   def checklevels(self):
      #if not len(self.DATA) == self.LEVELS:
      if len(self.DATA) < self.LEVELS:
         log.error("only %d/%d data lines loaded. Stop." % (len(self.DATA),self.LEVELS))
         import sys; sys.exit(9)


# -------------------------------------------------------------------
# Raso data class
# -------------------------------------------------------------------
class raso_data( object ):
   def __init__(self,data):
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
   def show(self,parameters,paramconfig,fid):

      tmpdata = []
      for rec in parameters: tmpdata.append("self.{0:s}".format(rec))
      tmpfmt  = []
      for rec in parameters: tmpfmt.append(paramconfig[rec]['format'])

      if fid:
         eval("fid.write(\'{0:s}\\n\' % tuple(({1:s})))".format(" ".join(tmpfmt),",".join(tmpdata))) 
      else:
         print eval("\'{0:s}\' % tuple(({1:s}))".format(" ".join(tmpfmt),",".join(tmpdata))) 


