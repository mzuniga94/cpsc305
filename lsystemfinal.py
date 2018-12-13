from pymel.core import *
import maya.cmds as cmds

# Variable for window name.
window_name = 'l_system_tree_window'

# Check if window exists.
if maya.cmds.window(window_name, exists=True):
    maya.cmds.deleteUI(window_name)

# Create the window and layout.
win = window(window_name, title='L-System Tree')

# Changes windo dimensions of window_name to widthHeight.
cmds.windowPref(window_name, widthHeight=(200, 200) )

layout = columnLayout(adjustableColumn=True)

# Gets the value of the int slider.
def getSliderValue():
    value = iterationSlider.getValue()
    return value

# Gets the axiom from the axiom drop down.  
def getAxiom():
    axiomValue = cmds.optionMenu('Axiom_OptionMenu', query=True, value=True)
    return axiomValue

# Get the angle of the tree branches.
def getAngle():
    angle = angleSlider.getValue()
    return angle

def getLength():
    length = lengthSlider.getValue()
    return length
    
# Calls and generates the tree by calling drawLSystem and getting values from sliders and drop downs.    
def generate_call_back(*args):
    drawLsystem(createLSystem(getSliderValue(), getAxiom()), getAngle(), getLength())    

# TODO: Add more axioms here if needed.
cmds.optionMenu('Axiom_OptionMenu', label='Axiom')
menuItem(label='F')
menuItem(label='X')

# UI Elements  
iterationSlider = intSliderGrp(l="Number of Iterations", min=1, max=5, field=True)
angleSlider = intSliderGrp(l="Angle", min=30, max=60, field=True)
lengthSlider = intSliderGrp(l="Length", min=1, max=5, field=True)
generateButton = button(label='Generate', height=200, command=generate_call_back)

def applyRules(ch):
    ruleStr = ""
    if ch == 'F':
        ruleStr = 'F[+F][<<<<+F][>>>>+F]'
    elif ch == 'X':
        ruleStr = 'X[+X][<<<+X][>>>+X]'
    else:
        ruleStr = ch
    return ruleStr

def processString(oldStr):
    newStr = ""
    for i in oldStr:
        newStr = newStr + applyRules(i)
    return newStr

def createLSystem(numIters, axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString
    return endString

def drawLsystem(instructions, angle, distance):
    parent = cmds.createNode("transform", n="L_Root_#")
    saved=[]
    for part in instructions:
        if part == 'F':
           cyl = cmds.cylinder(r=0.1, ax=[0,1,0], hr=1/0.1*distance)
           cyl = cmds.parent(cyl[0], parent, r=1)
           cmds.move(0, (distance/2.0), 0, cyl[0], os=1) 
           parent = cmds.createNode("transform", p=parent)
           cmds.move(0, (distance), 0, parent, os=1) 
        if part == 'X':
           cyl = cmds.cylinder(r=0.1, ax=[0,1,0], hr=1/0.1*distance)
           cyl = cmds.parent(cyl[0], parent, r=1)
           cmds.move(0, (distance/2.0), 0, cyl[0], os=1)
           parent = cmds.createNode("transform", p=parent)
           cmds.move(0, (distance), 0, parent, os=1)
        if part == '-':
           parent = cmds.createNode("transform", p=parent)
           cmds.rotate(angle, 0, 0, parent, os=1) 
        if part == '+':
           parent = cmds.createNode("transform", p=parent)
           cmds.rotate(-angle, 0, 0, parent, os=1) 
        if part == '<':
           parent = cmds.createNode("transform", p=parent)
           cmds.rotate(0, angle, 0, parent, os=1) 
        if part == '>':
           parent = cmds.createNode("transform", p=parent)
           cmds.rotate(0, -angle, 0, parent, os=1) 
        if part == '[':
           saved.append(parent)
        if part == ']':
           parent = saved.pop()  

win.show() 
