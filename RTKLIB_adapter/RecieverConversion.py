from BinaryCommand import *

class RecieverFormat(object):
    rtcm2 = 'rtcm2'
    rtcm3 = 'rtcm2'
    nov = 'nov'
    ubx = 'ubx'
    ss2 = 'ss2'
    hemis = 'hemis'
    stq = 'stq'
    javad = 'javad'
    nvs = 'nvs'
    binex = 'binex'
    rinex = 'rinex'

class Convbin(BinaryCommand):
    startTime = CommandPair('-ts', None) #-ts y/m/d h:m:s  start time [all] 
    endTime = CommandPair('-te', None) #-te y/m/d h:m:s  end time [all] 
    appTime = CommandPair('-tr', None) #-tr y/m/d h:m:s  approximated time for rtcm messages 
    dataInterval = CommandPair('-ti', None) #-ti tint  observation data interval (s) [all] 
    inputFormat = CommandPair('-r', None) #-r format log format type 
    recieverOptions = CommandPair('-ts', None) #-ro opt   receiver options 
    nrOfFrequencies = CommandPair('-ts', None) #-f freq   number of frequencies [2]
    ''' TO BE IMPLEMENTED:
    -hc comment  rinex header: comment line 
    -hm marker   rinex header: marker name 
    -hn markno   rinex header: marker number 
    -ht marktype rinex header: marker type 
    -ho observ   rinex header: observer name and agency separated by / 
    -hr rec      rinex header: receiver number, type and version separated by / 
    -ha ant      rinex header: antenna number and type separated by / 
    -hp pos      rinex header: approx position x/y/z separated by / 
    -hd delta    rinex header: antenna delta h/e/n separated by / 
    -v ver    rinex version [2.11] 
    -od       include doppler frequency in rinex obs [off] 
    -os       include snr in rinex obs [off] 
    -oi       include iono correction in rinex nav header [off] 
    -ot       include time correction in rinex nav header [off] 
    -ol       include leap seconds in rinex nav header [off] 
    -x sat    exclude satellite 
    -y sys    exclude systems (G:GPS,R:GLO,E:Galileo,J:QZSS,S:SBAS,C:BeiDou) 
    -d dir    output directory [same as input file] 
    -c staid  use RINEX file name convention with staid [off] 
    -o ofile  output RINEX OBS file 
    -n nfile  output RINEX NAV file 
    -g gfile  output RINEX GNAV file 
    -h hfile  output RINEX HNAV file 
    -q qfile  output RINEX QNAV file 
    -l lfile  output RINEX LNAV file 
    -s sfile  output SBAS message file
    '''
    def __init__(self, file, inputFormat):
        BinaryCommand.__init__(self, file, 'convbin.exe')
        self.inputFormat.argument = inputFormat


