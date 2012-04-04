'''
Created on Apr 3, 2012

@author: Dave Lee
'''

class HAL(object):
    '''
    classdocs
    '''

    NOTHING = "Nothing"

    GREEN = "Green"
    RED = "Red"
    YELLOW = "Yellow"
    BLUE = "Blue"
    ORANGE = "Orange"
    STRUM = "Strum"
    BACK = "Back"
    START = "Start"
    WHAMMY = "Whammy"
    EFFECT = "Effect"
    TILT = "Tilt"

    def __init__(self, buttonMap, axisMap, hatMap, axisDefault = {}, hatDefault = {}):
        '''
        Constructor
        '''
        self.buttonMap = buttonMap;
        self.axisMap = axisMap;
        self.hatMap = hatMap;
        
        self.axisDefault = axisDefault
        self.hatDefault = hatDefault
    
    def parseButton(self,joy):
        ret = {}
        numbutton = joy.get_numbuttons()
        for iB in range(0, numbutton):
                if(joy.get_button(iB)):
                    if iB in self.buttonMap:
                        ret[self.buttonMap[iB]] = True;
                    else:
                        print "Unrecognized Button {0} found.".format(iB)           
        return ret
    
    def parseAxis(self, joy):
        ret = {}
        numaxis = joy.get_numaxes()
        for iA in range(0, numaxis):
                defaultValue = 0.0
                if iA in self.axisDefault:
                    defaultValue = self.axisDefault[iA]
                                        
                if(joy.get_axis(iA) != defaultValue):
                    if iA in self.axisMap:
                        ret[self.axisMap[iA]] = joy.get_axis(iA);
                    else:
                        print "Unrecognized Axis {0} found.".format(iA)
        return ret
    
    def parseHat(self, joy):
        ret = {}
        numhat = joy.get_numhats()
        for iH in range(0, numhat):
                defaultValue = 0.0
                if iH in self.hatDefault:
                    defaultValue = self.hatDefault[iH]
                if(joy.get_hat(iH) != defaultValue):
                    if iH in self.hatMap:
                        ret[self.hatMap[iH]] = joy.get_hat(iH);
                    else:
                        print "Unrecognized Hat {0} found.".format(iH)
        return ret
    
    def parseAll(self, joy):
        ret = {}
        ret.update(self.parseButtons(joy))
        ret.update(self.parseAxis(joy))
        ret.update(self.parseHat(joy))
        return ret
    
    