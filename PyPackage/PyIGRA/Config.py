# -------------------------------------------------------------------
# - NAME:        Config.py
# - AUTHOR:      Reto Stauffer
# - DATE:        2017-02-06
# -------------------------------------------------------------------
# - DESCRIPTION:
# -------------------------------------------------------------------
# - EDITORIAL:   2017-02-06, RS: Created file on thinkreto.
# -------------------------------------------------------------------
# - L@ST MODIFIED: 2017-02-06 17:03 on pc24-c707
# -------------------------------------------------------------------

# Initialize logger
import logging
log = logging.getLogger('PyIGRA.Config')

class Config( object ):

   def __init__(self,file=None):

      import sys, os, pkg_resources, ConfigParser, re

      # Optparse
      from optparse import OptionParser
      parser = OptionParser()
      parser.add_option("-l", "--limit", dest="limit", default=None, type="int",
                        help="Test/development option. Will only print the first -l/--limit entries")
      parser.add_option("-i", "--id", dest="station_id", default=None,
                        help="Station identifier which should be processed.")
      parser.add_option("-o", "--output", dest="outputfile", default=None,
                        help="Filename. If set the output will be saved in this file. " + \
                             "If not set stdout is used.")
      parser.add_option("-p", "--parameters", dest="parameters", default=None,
                        help="Comma separated list of strings which specify the parameters " + \
                             "which should be printed. If not set, the ones from the config " + \
                             "(or default config) will be used.")
      
      (options, args) = parser.parse_args()

      # Append options to class
      for key in options.__dict__.keys(): setattr(self,key,options.__dict__[key])

      # Required
      if not options.station_id:
         log.error("Input -i/--id not set. See also: PyIGRA_search"); sys.exit(9)
      self.station_id = self.station_id.upper()

      # If no input "file" is given: read ing
      # default config file (included in package source)
      if not file:
         resource_package = os.path.dirname(__file__) 
         log.debug("Package path is \"{0:s}\"".format(resource_package))
         file = os.path.join(resource_package,'config','default.conf')

      # Read config file
      CNF = ConfigParser.ConfigParser()
      CNF.read(file)
      try:
         self.url        = CNF.get("main","url")
         self.statlist   = CNF.get("main","statlist")
         self.rehead     = CNF.get("regex","head")
         self.redata     = CNF.get("regex","data")
      except Exception as e:
         log.error(e); sys.exit(9)

      # If input -p/--parameters not set: use the one from the config file
      if not self.parameters:
         self.parameters = CNF.get("main","parameters")
      tmp = self.parameters; self.parameters = []
      for rec in tmp.split(","): self.parameters.append(rec.strip().upper())

      # Reading parameters config
      self.paramconfig = {}
      for sec in CNF.sections():
         mtch = re.match("^parameters\ (.*)$",sec)
         if not mtch: continue
         # Else read config
         self.paramconfig[mtch.group(1)] = {'format':'%s'}
         try:
            self.paramconfig[mtch.group(1)]['format'] = CNF.get(sec,"format")
         except:
            log.debug("No format specification in \"{0:s}\", take default".format(sec))

      # Some output
      log.debug("Data URL: {0:s}".format(self.url))
      log.debug("Statlist URL: {0:s}".format(self.statlist))
















