"""
CUSTOM HEADS UP DISPLAY PYMEL MODULE FOR MAYA
DONE BY DANIEL SANCHEZ QUIROS, 3danimanimal@gmail.com
"""
import pymel.core as pm

class Custom_hud():
    def __init__(self):
        """
        Initialize required data
        """
        self.AnimatorName = "Daniel"
        self.Date = pm.date(format = "DD/MM/YYYY")
        self.SceneName = "prueba"
        #self.window = pm.window(menuBar = False, widthHeight = [300, 200])
        self.activesHuds = []
        self.__init_window__()
    
    def createHud(self):
        self.activesHuds.append(int(pm.headsUpDisplay("AnimatorName", label= self.AnimatorName, labelFontSize = "small", section = 5, block = 1)))
        self.activesHuds.append(int(pm.headsUpDisplay("Date", label= self.Date, labelFontSize = "small", section = 6,block = 1)))
        self.activesHuds.append(int(pm.headsUpDisplay("SceneName", label= self.SceneName, labelFontSize = "small", section = 7,block = 1)))
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
        self.window = pm.window(menuBar = False, widthHeight = [300, 200])
        self.columna = pm.columnLayout(adjustableColumn = True)
        self.row1 = pm.rowLayout(numberOfColumns=3, adjustableColumn = True, parent = self.columna)
        pm.text("Name:", parent = self.row1)
        self.nameQ = pm.textField(parent = self.row1)
        pm.button(parent = self.row1)
        self.row2 =pm.rowLayout(numberOfColumns=3, adjustableColumn = True, parent = self.columna)
        pm.text("Scene Name")
        self.sceneNameQ = pm.textField(parent = self.row2)
        pm.button(parent = self.row2)
        pm.showWindow(self.window)