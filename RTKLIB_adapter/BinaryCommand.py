from Utils import *
import subprocess

class BinaryCommand(object):
    __filePath__ = ''     # input receiver binary log file 
    __appName__ = ''
    def __init__(self, file, appName):
        self.__filePath__ = file
        self.__appName__ = appName
    def toString(self):
        classAttributes = [a for a in dir(self) if not a.startswith('__') and not callable(getattr(self, a))]
        commandList = [self.__appName__]
        for attributeString in classAttributes:
            attribute = getattr(self, attributeString)
            if attribute.argument != None:
                commandList.append(attribute.toString())
        commandList.append(self.__filePath__)
        return CommandListString(commandList)
    def run(self):
        return runCommand(self.toString())

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
    def toString(self):
        if self._command != None and self.argument != None:
            return self._command + " " + self.argument
        else:
            return None