import sys, os

# https://stackoverflow.com/questions/1296501/find-path-to-currently-running-file
# This only works in Python terminal
def getLibraryFolderPath(relativePath = ""):
    path = os.path.dirname(sys.argv[0])+relativePath
    path = path.replace('/','\\')
    return path
    #return os.chdir(sys.argv[0])

def getAbsolutePath2(relativePath = ""):
    path = os.path.abspath(relativePath)
    return path
    #return os.chdir(sys.argv[0])