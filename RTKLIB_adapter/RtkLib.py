from Utils import *
from BinaryCommand import *
from RecieverConversion import Convbin, RecieverFormat

def rnx2rtkp():
    return runCommand('rnx2rtkp.exe')

def rtkconv():
    return runCommand('rtkconv.exe')

def convbin(rawDataPath, recieverFormat = RecieverFormat.ubx):
    if not isinstance(recieverFormat, RecieverFormat):
        raise TypeError('Reciever format is invalid!')

    commandList = ['convbin.exe']

    if recieverFormat != RecieverFormat.unknown:
        commandList.append('-r')
        commandList.append(recieverFormat._value_)
    commandList.append(rawDataPath)
    print(commandList)
    return runCommand(CommandListString(commandList))

if __name__ == '__main__':
    rawDataPath = getLibraryFolderPath('/testFiles/HavfruenBow.ubx', PathEmbrasing='"')
    #convbin(rawDataPath, RecieverFormat.ubx)
    test = Convbin(rawDataPath, RecieverFormat.ubx)
    print(test.toString())
    test.run()

