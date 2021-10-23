import sys, os
import subprocess

# https://stackoverflow.com/questions/1296501/find-path-to-currently-running-file
# This only works in Python terminal
def getLibraryFolderPath(relativePath = "", dirSeperator = '\\', PathEmbrasing = ""):
    path = os.path.dirname(sys.argv[0])+relativePath
    path = path.replace('/', dirSeperator)
    return PathEmbrasing + path + PathEmbrasing
    #return os.chdir(sys.argv[0])

def getAbsolutePath2(relativePath = ""):
    path = os.path.abspath(relativePath)
    return path
    #return os.chdir(sys.argv[0])

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
            return ''