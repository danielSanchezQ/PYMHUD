"""CUSTOM HUD FOR MAYA
 BY DANIEL SANCHEZ QUIROS"""

import pymel.core as pm


def custom_hud(names):
    """TESTING"""
    pm.headsUpDisplay("Current_Camera", section = 1, block = 2, label= "position", labelFontSize = "small")

"""MORE TESTING"""	
cameraHUD = custom_hud("names")	
pm.headsUpDisplay("Current_Camera", rem = True)