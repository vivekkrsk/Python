class tv:
    def __init__(self):
        self.channel = 1
        self.volumelevel =1
        self.on = False

    def turnOn(self):
        self.on = True

    def turnOff(self):
        self.on = False

    def getChannel(self):
        return self.channel

    def setChannel(self,channel):
        if self.on and 1 <= self.channel <= 120:
            self.channel = channel

    def getVolumeLevel(self):
        return self.volumelevel

    def setVolume(self, volumeLevel):
        if self.on and 1<= self.volumelevel <= 7 :
            self.volumelevel = volumeLevel   

    def channelUp(self):
        if self.on and self.channel < 120:
            self.channel +=1
    
    def channelDown(self):
        if self.on and self.channel >1:
            self.channel -=1

    def volumeUp(self):
        if self.on and self.volumelevel< 7:
            self.volumelevel +=1

    def volumeDown(self):
        if self.on and self.volumelevel >1 :
            self.volumelevel -=1