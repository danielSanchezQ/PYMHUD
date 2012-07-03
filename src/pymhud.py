"""
CUSTOM HEADS UP DISPLAY PYMEL MODULE FOR MAYA
DONE BY DANIEL SANCHEZ QUIROS, 3danimanimal@gmail.com
"""
import pymel.core as pm
from pymel.core.windows import Callback

class Custom_hud():
    def __init__(self):
        """
        Initialize required data
        """
        self.AnimatorName = "Daniel"
        self.Date = pm.date(format = "DD/MM/YYYY")
        self.SceneName = "PYMHUD"
        self.activesHuds = []
        self.__init_window__()
    
    def queryData(self):
        self.AnimatorName = self.nameQ.getText()
        self.SceneName = self.sceneNameQ.getText()
        
    def createHud(self):
        self.activesHuds.append(int(pm.headsUpDisplay("AnimatorName", label = self.AnimatorName, labelFontSize = "small", section = 5, block = 1)))
        self.activesHuds.append(int(pm.headsUpDisplay("Date", label= self.Date, labelFontSize = "small", section = 6,block = 1)))
        self.activesHuds.append(int(pm.headsUpDisplay("SceneName", label = self.SceneName, labelFontSize = "small", section = 7,block = 1)))
        self.frameHud()
        
    def frameHud(self):
        pm.mel.eval("setCurrentFrameVisibility(!`optionVar -q currentFrameVisibility`)")
        
    def nameHud(self, state = True):
        self.queryData()
        if state:
            self.activesHuds.append(int(pm.headsUpDisplay("AnimatorName", label = self.AnimatorName, labelFontSize = "small", section = 5, block = 1)))
        else:
            pm.headsUpDisplay("AnimatorName", rem = True)
    
    def sceneHud(self, state = True):
        self.queryData()        
        if state:
            self.activesHuds.append(int(pm.headsUpDisplay("SceneName", label = self.SceneName, labelFontSize = "small", section = 7,block = 1)))
        else:
            pm.headsUpDisplay("SceneName", rem = True)    
    
    def dateHud(self, state = True):
        if state:
            self.activesHuds.append(int(pm.headsUpDisplay("Date", label= self.Date, labelFontSize = "small", section = 6,block = 1)))        
        else:
            pm.headsUpDisplay("Date", rem = True)
            
    def removeAll(self):
        for i in self.activesHuds:
            pm.headsUpDisplay(rid = i)
        self.activesHuds =  []
        
    def destroyWindow(self):
        pm.deleteUI(self.window, window = True)
        
    def __init_window__(self):
        self.window = pm.window(menuBar = False, widthHeight = [200, 100], title = "PYMHUD by Daniel Sánchez Quirós")
        self.columna = pm.columnLayout(adjustableColumn = True)
        #Name row
        self.row1 = pm.rowLayout(numberOfColumns=3, adjustableColumn = True, parent = self.columna)
        pm.text("Name:",al = "left", parent = self.row1)
        self.nameQ = pm.textField(parent = self.row1)
        pm.checkBox(label = "", parent = self.row1, offCommand = Callback(self.nameHud, False), onCommand = Callback(self.nameHud, True))
        #Scene row
        self.row2 = pm.rowLayout(numberOfColumns=3, adjustableColumn = True, parent = self.columna)
        pm.text("Scene Name:",al = "left")
        self.sceneNameQ = pm.textField(parent = self.row2)
        pm.checkBox(label = "", parent = self.row2, offCommand = Callback(self.sceneHud, False), onCommand = Callback(self.sceneHud, True))
        #Date row
        self.row3 = pm.rowLayout(numberOfColumns=3, adjustableColumn = True, parent = self.columna)
        pm.text("Date:",al = "left")
        pm.checkBox(label = "", parent = self.row3, offCommand = Callback(self.dateHud, False), onCommand = Callback(self.dateHud, True))
        #rame counter row
        self.row4 = pm.rowLayout(numberOfColumns=3, adjustableColumn = True, parent = self.columna)
        pm.text("Frame Counter:",al = "left")
        pm.checkBox(label = "", parent = self.row4, offCommand = Callback(self.frameHud), onCommand = Callback(self.frameHud))
        pm.showWindow(self.window)
        
    def __del__(self):
        self.removeAll()
        self.destroyWindow()