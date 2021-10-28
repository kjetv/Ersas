from Utils import *
from abc import ABC, abstractmethod
import subprocess

class BinaryCommand(ABC):
    @abstractmethod
    def firstCommands(self):
        pass
    @abstractmethod
    def lastCommands(self):
        pass
    def __str__(self):
        commandList = []
        commandList += self.firstCommands()
        commandList += self.options()
        commandList += self.lastCommands()
        return CommandListString(commandList)
    def run(self):
        return runCommand(self.__str__())
    # Options, lists all attributes that don't have __ and are independent from order when CUI is used
    def options(self):
        commandList = []
        classAttributes = [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
        for attributeString in classAttributes:
            attribute = getattr(self, attributeString)
            if isinstance(attribute,CommandPair):
                if attribute != None:
                    commandList.append(str(attribute))
        return commandList

class GNSSFormat(object):
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

def CommandListString(commandList):
        commandString = ""
        for commandNr in range(len(commandList)):
            if commandNr == len(commandList) - 1:
                commandString += commandList[commandNr]
            else:
                commandString += commandList[commandNr] + " "
        return commandString

class CommandPair(object):
    _command = None
    argument = None
    def __init__(self, command, argument):
        self._command = command
        self.argument = argument
    def __str__(self):
        if self != None:
            return self._command + " " + self.argument
        else:
            return None
    def __eq__(self, obj):
        return obj == self.argument