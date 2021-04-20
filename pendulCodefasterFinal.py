import FreeCAD
import FreeCADGui
from PySide import QtGui,QtCore
import math

angleRot = 0 #rod angle rotation for pendul motion in Sketch
varRod = 0 #counter to incremant angle rotation of rod in Python
swing = 0
escapeRot = 0
escapeRotation = 0

def update():
	global angleRot, varRod, swing, escapeRot, escapeRotation

#rod animation, the motor driving the anchor in the master sketch
	FreeCAD.getDocument('pendul').getObject('Variables').varRod = varRod
	#incremant counter angle of rod
	varRod+=1

	swing = 6.5 * math.cos(math.radians(varRod)) #varRod degre to radians, then cos of angle

	FreeCAD.getDocument('pendul').getObject('Variables').swing = swing	

#reset value after one full rotation of rod, so can use value to start and stop anchor motion
	if FreeCAD.getDocument('pendul').getObject('Variables').varRod == 360:
		varRod = 1

# motion left to right of pendulum	

	if 140 < FreeCAD.getDocument('pendul').getObject('Variables').varRod <= 320:
		FreeCAD.getDocument('pendul').getObject('Variables').escapeRotation  = escapeRot
		escapeRot = escapeRot + math.sin(math.radians(varRod)) * 1/15

# motion right to left of pendulum	

	if  FreeCAD.getDocument('pendul').getObject('Variables').varRod > 320 or FreeCAD.getDocument('pendul').getObject('Variables').varRod <= 140:
		FreeCAD.getDocument('pendul').getObject('Variables').escapeRotation  = escapeRot
		escapeRot = escapeRot - math.sin(math.radians(varRod)) * 1/15
#to speed up added the if statement, redraw only one in 10 degree
	if FreeCAD.getDocument('pendul').getObject('Variables').varRod % 10 == 0:	
		App.getDocument('pendul').recompute()
	

timer = QtCore.QTimer()
timer.timeout.connect(update)

timer.start()



timer.stop()
