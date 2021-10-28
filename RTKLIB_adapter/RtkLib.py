from Utils import *
from BinaryCommand import *
from PostProcessing import *
from RinexConverter import Convbin
from Sensors import Sensor, GNSS
import glob

class RTKLIB(object):

    def __init__(self, sensorDataFolder):
        self.roverFile = roverFile
        self.baseFile = baseFile
        self.navFile = navFile

    def rnx2rtkp():
        return runCommand('rnx2rtkp.exe')

    def rtkconv():
        return runCommand('rtkconv.exe')

    def postProcessRawData(rawDataPath):
        rinex = Convbin(rawDataPath)
        process = Rnx2rtkp()


if __name__ == '__main__':
    rawDataPath = getLibraryFolderPath('/testFiles/Gunnerus_bow')
    print(rawDataPath)
    text_files = getFileList(rawDataPath)
    print(text_files)


