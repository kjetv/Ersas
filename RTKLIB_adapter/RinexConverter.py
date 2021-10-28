from BinaryCommand import *

class Convbin(BinaryCommand):
    startTime =                 CommandPair('-ts', None)     # y/m/d h:m:s  start time [all] 
    endTime =                   CommandPair('-te', None)     # y/m/d h:m:s  end time [all] 
    appTime =                   CommandPair('-tr', None)     # y/m/d h:m:s  approximated time for rtcm messages 
    dataInterval =              CommandPair('-ti', None)     # tint  observation data interval (s) [all] 
    inputFormat =               CommandPair('-r', None)      # format log format type 
    recieverOptions =           CommandPair('-ts', None)     # opt   receiver options 
    nrOfFrequencies =           CommandPair('-ts', None)     # freq   number of frequencies [2]
    headCommentLine =           CommandPair('-hc', None)     # rinex header: comment line 
    headMarkerName =            CommandPair('-hm', None)     # rinex header: marker name 
    headMarkerNumber =          CommandPair('-hn', None)     # rinex header: marker number 
    headMarkerType =            CommandPair('-ht', None)     # rinex header: marker type 
    headObserverAgency =        CommandPair('-ho', None)     # rinex header: observer name and agency separated by / 
    headReciever =              CommandPair('-hr', None)     # rinex header: receiver number, type and version separated by / 
    headAntenna =               CommandPair('-ha', None)     # rinex header: antenna number and type separated by / 
    headPosition =              CommandPair('-hp', None)     # rinex header: approx position x/y/z separated by / 
    headAntennaDelta =          CommandPair('-hd', None)     # rinex header: antenna delta h/e/n separated by / 
    RinexVersion =              CommandPair('-v', None)      # rinex version [2.11] 
    includeDoppler =            CommandPair('-od', None)     # include doppler frequency in rinex obs [off] 
    includeSNR =                CommandPair('-os', None)     # include snr in rinex obs [off] 
    includeIONO =               CommandPair('-oi', None)     # include iono correction in rinex nav header [off] 
    includeTimeCorrection =     CommandPair('-ot', None)     # include time correction in rinex nav header [off] 
    includeLeapSeconds=         CommandPair('-ol', None)     # include leap seconds in rinex nav header [off] 
    exclueSatellite=            CommandPair('-x', None)      # exclude satellite 
    excludeSatelliteSystems=    CommandPair('-y', None)      # exclude systems (G:GPS,R:GLO,E:Galileo,J:QZSS,S:SBAS,C:BeiDou) 
    outputDirectory =           CommandPair('-d', None)      # output directory [same as input file] 
    RinexFileNameConvention =   CommandPair('-c', None)      # use RINEX file name convention with staid [off] 
    OBSfile =                   CommandPair('-o', None)      # output RINEX OBS file 
    NAVfile =                   CommandPair('-n', None)      # output RINEX NAV file 
    GNAVfile =                  CommandPair('-g', None)      # output RINEX GNAV file 
    HNAVfile =                  CommandPair('-h', None)      # output RINEX HNAV file 
    QNAVfile =                  CommandPair('-q', None)      # output RINEX QNAV file 
    LNAVfile =                  CommandPair('-l', None)      # output RINEX LNAV file 
    SBASfile =                  CommandPair('-s', None)      # output SBAS message file
    __inputFile__ =             []
    __appName__   =             ["convbin.exe"]
    def __init__(self, file):
        self.__inputFile__ = [file]
    def firstCommands(self):
        return self.__appName__
    def lastCommands(self):
        return self.__inputFile__


