import subprocess
from enum import Enum
from sys import stderr
from Utils import *

class RecieverFormat(Enum):
    unknown = None
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

#https://stackoverflow.com/questions/2231227/python-subprocess-popen-with-a-modified-environment
def runCommand(cmd, path=getLibraryFolderPath("/bin")):
    p1 = subprocess.Popen(args = cmd, cwd = path, shell = True)
    p1.wait()
    if p1.returncode != 0:
        raise p1.stderr
    return p1.stderr

def rnx2rtkp():
    return runCommand('rtkconv.exe')

def rtkconv():
    return runCommand('rtkconv.exe')

def convbin(rawDataPath, recieverFormat = RecieverFormat.unknown):
    if not isinstance(recieverFormat, RecieverFormat):
        raise TypeError('Reciever format is invalid!')
    if recieverFormat == RecieverFormat.unknown:
        return runCommand('convbin.exe' + ' "' + rawDataPath + '"')
    else:
        return runCommand('convbin.exe -r ' + recieverFormat._value_ + ' "' + rawDataPath + '"')

if __name__ == '__main__':
    rawDataPath = getLibraryFolderPath('/testFiles/GunnerusBow.txt')
    convbin(rawDataPath)

