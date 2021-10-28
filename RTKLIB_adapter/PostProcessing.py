from BinaryCommand import *

class Rnx2rtkp(BinaryCommand):
    printHelp =                 CommandPair('-?', None)
    configFile =                CommandPair('-k', None)     #input options from configuration file [off] 
    outputFile =                CommandPair('-o', None)     #set output file [stdout]
    startTime =                 CommandPair('-ts',None)     #ds ts start day/time (ds=y/m/d ts=h:m:s) [obs start time] 
    endTime =                   CommandPair('-te',None)     #de te end day/time   (de=y/m/d te=h:m:s) [obs end time] 
    dataInterval =              CommandPair('-ti',None)     #time interval (sec) [all] 
    mode =                      CommandPair('-p', None)     #mode (0:single,1:dgps,2:kinematic,3:static,4:moving-base,5:fixed,6:ppp-kinematic,7:ppp-static) [2] 
    elevationMask =             CommandPair('-m', None)     #elevation mask angle (deg) [15] 
    frequencies =               CommandPair('f',  None)     #number of frequencies for relative mode (1:L1,2:L1+L2,3:L1+L2+L5) [2] 
    validTreshold =             CommandPair('v',  None)     #validation threshold for integer ambiguity (0.0:no AR) [3.0] 
    backwardSolution =          CommandPair('-b', None)     #backward solutions [off] 
    forwardBackwardSolution =   CommandPair('-c', None)     #forward/backward combined solutions [off] 
    instaIntAmbRes =            CommandPair('-i', None)     #instantaneous integer ambiguity resolution [off] 
    fixHoldForInstaIntAmbRes =  CommandPair('-h', None)     #fix and hold for integer ambiguity resolution [off] 
    outputECEF =                CommandPair('-e', None)     #output x/y/z-ecef position [latitude/longitude/height] 
    outputENU =                 CommandPair('-a', None)     #output e/n/u-baseline [latitude/longitude/height] 
    outputNMEA =                CommandPair('-n', None)     #output NMEA-0183 GGA sentence [off] 
    outputLatLonForm =          CommandPair('-g', None)     #output latitude/longitude in the form of ddd mm ss.ss [ddd.ddd] 
    outputTimeForm =            CommandPair('-t', None)     #output time in the form of yyyy/mm/dd hh:mm:ss.ss [sssss.ss] 
    outputTimeInUTC =           CommandPair('-u', None)     #output time in utc [gpst] 
    timeDecimals =              CommandPair('-d', None)     #number of decimals in time [3] 
    fieldSeperator =            CommandPair('-s', None)     #field separator [' '] 
    baseReferenceECEF =         CommandPair('-r', None)     #reference (base) receiver ecef pos (m) [average of single pos] 
    baseReferenceLLH =          CommandPair('-l', None)     #reference (base) receiver latitude/longitude/height (deg/m) 
    outputSolutionStatus =      CommandPair('-y', None)     #output solution status (0:off,1:states,2:residuals) [0] 
    debugTraceLevel =           CommandPair('-x', None)     #debug trace level (0:off) [0] 
    
    #Read RINEX OBS/NAV/GNAV/HNAV/CLK, SP3, SBAS message log files and compute receiver (rover) 
    #positions and output position solutions. 
    #The first RINEX OBS file shall contain receiver (rover) observations. For the relative mode, the second 
    #RINEX  OBS  file  shall  contain  reference  (base  station)  receiver  observations.  At  least  one  RINEX 
    #NAV/GNAV/HNAV file shall be included in input files
    __inputFiles__ =            [] 
    __appName__   =             ["rnx2rtkp.exe"]
    def __init__(self, files):
        self.__inputFiles__ = files
    def firstCommands(self):
        return self.__appName__
    def lastCommands(self):
        return CommandListString(self.__inputFiles__)