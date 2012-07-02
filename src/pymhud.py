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
        self.SceneName = "prueba"
        self.activesHuds = []
        self.__init_window__()
    
    def createHud(self):
        self.activesHuds.append(int(pm.headsUpDisplay("AnimatorName", label = self.AnimatorName, labelFontSize = "small", section = 5, block = 1)))
        self.activesHuds.append(int(pm.headsUpDisplay("Date", label= self.Date, labelFontSize = "small", section = 6,block = 1)))
        self.activesHuds.append(int(pm.headsUpDisplay("SceneName", label = self.SceneName, labelFontSize = "small", section = 7,block = 1)))
        self.frameHud()
        
    def frameHud(self):
        test = pm.mel.eval("setCurrentFrameVisibility(!`optionVar -q currentFrameVisibility`)")
        print test
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
        pm.checkBox(label = "", parent = self.row1)
        #Scene row
        self.row2 = pm.rowLayout(numberOfColumns=3, adjustableColumn = True, parent = self.columna)
        pm.text("Scene Name:",al = "left")
        self.sceneNameQ = pm.textField(parent = self.row2)
        pm.checkBox(label = "", parent = self.row2)
        #Date row
        self.row3 = pm.rowLayout(numberOfColumns=3, adjustableColumn = True, parent = self.columna)
        pm.text("Date:",al = "left")
        pm.checkBox(label = "", parent = self.row3)
        #rame counter row
        self.row4 = pm.rowLayout(numberOfColumns=3, adjustableColumn = True, parent = self.columna)
        pm.text("Frame Counter:",al = "left")
        pm.checkBox(label = "", parent = self.row4,ofc = Callback(self.frameHud), onCommand = Callback(self.frameHud))
        pm.showWindow(self.window)
        
    def __del__(self):
        pass