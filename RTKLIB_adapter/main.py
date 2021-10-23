import subprocess, sys, os

#Can either ut shell = true, or shell = false but then the environment and path must be spesified
#https://stackoverflow.com/questions/2231227/python-subprocess-popen-with-a-modified-environment
def runCommand(cmd, path):
    #p1 = subprocess.Popen(cmd, shell = True)
    p1 = subprocess.Popen(args = cmd, cwd = path, shell = True)
    p1.wait()
    if p1.returncode == 0:
        print('command : Success')
    else:
        print('command : Failed')

def rnx2rtkp():
    cmd =  'rtkconv.exe'
    runCommand(cmd, getAbsolutePath("/bin"))

def rtkconv():
    cmd = 'rtkconv.exe'
    runCommand(cmd,  getAbsolutePath("/bin"))

def convbin(rawDataPath):
    cmd = 'convbin.exe -r ubx ' + '"' + rawDataPath + '"'
    #cmd = 'convbin.exe -r ubx GunnerusBow.txt'
    runCommand(cmd,  getAbsolutePath("/bin"))

# https://stackoverflow.com/questions/1296501/find-path-to-currently-running-file
def getAbsolutePath(relativePath = ""):
    path = os.path.dirname(sys.argv[0])+relativePath
    print(path)
    return path
    #return os.chdir(sys.argv[0])

if __name__ == '__main__':
    #cmd = "df -h"
    #data = "r"+repr(getAbsolutePath("/testFiles/GunnerusBow.txt"))
    rawDataPath = getAbsolutePath('/testFiles/GunnerusBow.txt')
    #print(data)
    #rtkconv()
    convbin(rawDataPath)
    #rnx2rtkp()
