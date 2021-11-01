import sys, os

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

def getFileList(path):
    return os.listdir(path)

def getDataPath(dataDirectory, fileName, fileFormat):
    dataDirectory = os.path.dirname(rawDataPath)
    directoryFiles = getFileList(dataDirectory)
    