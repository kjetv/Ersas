from abc import ABC, abstractmethod
import numpy as np

class Sensor(ABC):
    def __init__(self):
        self.samplingTime = self.getSamplingTime()
        self.noise = self.getNoise()
        self.timeStamps = self.getTimeStamps()
    @abstractmethod
    def getSamplingTime():
        return 0
    @abstractmethod
    def getNoise():
        return 0
    @abstractmethod
    def getTimeStamps():
        return [0,0,0]

class GNSS(ABC):
    def __init__(self):
        self.linearisationPoint = self.getLinearisationPoint()
        self.NEDPositions = self.getNEDPositions()
        self.LLHPositions = self.getLLHPositions()
        self.VerticalUncertanty = self.getVerticalUncertanty()
        self.HorisontalUncertanty = self.getHorisontalUncertanty()
    @abstractmethod
    def getLinearisationPoint():
        return [0,0,0]
    @abstractmethod
    def getNEDPositions():
        return [0,0,0]
    @abstractmethod
    def getLLHPositions():
        return [0,0,0]
    @abstractmethod
    def getVerticalUncertanty():
        return 0
    @abstractmethod
    def getHorisontalUncertanty():
        return 0



