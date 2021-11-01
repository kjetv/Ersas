class ExperimentData(object):
    baseFile = None
    navFile = None
    roverFiles = None
    experimentPath = None
    def __init__(self, directoryPath):
        self.dirPath = directoryPath
        self.convertExperimentDataToRinex()
        self.baseFile = self.getBaseFile()
        self.navFile = self.getNavFile()
        self.roverFiles = self.getRoverFiles()
        self.postProcessData()
    def convertExperimentDataToRinex():
        pass
    def postProcessData():
        pass
    def getBaseFile():
        return None
    def getNavFile():
        return None
    def getRoverFiles():
        return None
    def getData():
        pass
