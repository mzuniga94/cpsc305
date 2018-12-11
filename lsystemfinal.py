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
cmds.windowPref(window_name, widthHeight=(800, 800) )

layout = columnLayout(adjustableColumn=True)

generateTreeButton = button(label='Generate!', height=200)
cmds.frameLayout(label='Axiom')

# Create an option menu.
# TODO: Learn how to GET values from options.
# Get item from menuItem as Axiom in our L-system.
cmds.optionMenu('Axiom_OptionMenu', label='')
menuItem(label='Axiom1')
menuItem(label='Axiom2')
menuItem(label='Axiom3')

cmds.optionMenu(label='Rule')
menuItem(label='Rule1')
menuItem(label='Rule2')
menuItem(label='Rule3')

cmds.optionMenu(label='Color')
menuItem(label='Red')
menuItem(label='Blue')
menuItem(label='Yellow')

# Testing for whether it gets the value from the option menu.
def axiomTestCallback(*args):
    axiomValue=cmds.optionMenu('Axiom_OptionMenu', query=True, value=True)
    print(axiomValue)
    
testButton = button(label='Print Axiom Test to screen', height=200, command=axiomTestCallback)


# Set the number of iterations.
iterSlider = intSliderGrp(l = "Number of Iterations", min=0, max=10, field=True)

# Create axioms.
def createLSystem(numIters, axiom):
    startString = axiom
    endString = " "
    for i in range(numIters):
        endstring = processString(startString)
        startString = endString
    return endString

# Create rules for L-system.
def processString(oldStr):
    newStr = " "
    for ch in oldStr:
        newStr = newStr + applyRules(ch)
    return newStr
    
def applyRules(ch):
    newstr = ""
    if ch == 'X':
        newstr = 'F+[[X]-X]-F[-FX]+X'   # Rule 1
    elif ch == 'F':
        newstr = 'FF'  # Rule 2
    else:
        newstr = ch    # no rules apply so keep the character
    return newstr
    
def drawLsystem(instructions, angle, distance):
    parent = maya.cmds.createNode("transform", n="L_Root_#")
    info_list = []
    for cmd in instructions:
        if cmd == 'F':
            cyl = cmds.cylinder(r=0.1, ax=[0,1,0], hr=1/0.1*distance)
            cyl = cmds.parent( cyl[0], parent, r=1)
            cmds.move(0, (distance/2.0), 0, cyl[0], os=1) 
            parent = cmds.createNode("transform", p=parent)
            cmds.move(0, (distance), 0, parent, os=1)
        elif cmd == '+':
            parent = cmds.createNode("transform", p=parent)
            cmds.rotate(-angle, 0, 0, parent, os=1)
        elif cmd == '-':
            parent = cmds.createNode("transform", p=parent)
            cmds.rotate(angle, 0, 0, parent, os=1)
        elif cmd == '[':
            info_list.append(parent)
        elif cmd == ']':
            new_info = info_list.pop() #<- might not need this, we will see
            parent = saved.pop()

win.show()
