from Utils import *
from BinaryCommand import *
from PostProcessing import *
from RinexConverter import Convbin
from Sensors import Sensor, GNSS


def postProcessRawData(rawDataPath, baseData = None, dataFormat = 'ubx'):
    conv = Convbin(rawDataPath)
    conv.inputFormat.argument = dataFormat
    conv.run()

    if




if __name__ == '__main__':
    rawData = getLibraryFolderPath('/testFiles/Experiment/GunnerusBow.txt', PathEmbrasing='"')
    outputData = getLibraryFolderPath('/testFiles/Experiment/GunnerusBow.pos', PathEmbrasing='"')
    boatObs = getLibraryFolderPath('/testFiles/Experiment/GunnerusBow.obs', PathEmbrasing='"')
    boatNav = getLibraryFolderPath('/testFiles/Experiment/GunnerusBow.nav', PathEmbrasing='"')
    baseNav = getLibraryFolderPath('/testFiles/Experiment/trds1240.21n', PathEmbrasing='"')
    baseObs = getLibraryFolderPath('/testFiles/Experiment/trds1240.21o', PathEmbrasing='"')


    #conv = Convbin(rawData)
    #conv.inputFormat.argument = 'ubx'
    #print(conv)
    #conv.run()
    post = Rnx2rtkp([boatObs, baseObs, baseNav])
    #post.mode.argument = '0'
    post.outputFile.argument = outputData
    print(post)
    post.run()

