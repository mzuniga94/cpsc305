from pymel.core import *
import maya.cmds

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
menuItem(label='1')
menuItem(label='Axiom2')
menuItem(label='Axiom3')

cmds.optionMenu('Rule_OptionMenu', label='Rule')
menuItem(label='1')
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

def generate_callback_button(*args):
	axiom=cmds.optionMenu('Axiom_OptionMenu', query=True, value=True)
	axiomValue = int(axiom)
	rule=cmds.optionMenu('Rule_OptionMenu', query=True, value=True)
	ruleValue = int(rule)
	n = treeIterSlider.getValue() # Get value of slider input
	print(axiomValue)
	print(ruleValue)
	print(n)

# Test buttons
testButton2 = button(label='Print Test', height=200, command=generate_callback_button)
testButton = button(label='Print Axiom Test to screen', height=200, command=axiomTestCallback)

# Set the number of iterations.
treeIterSlider = intSliderGrp(l = "Number of Iterations", min=1, max=5, field=True)
iterSlider = intSliderGrp(l = "Number of Iterations", min=1, max=5, field=True)

# Create axioms.

# Create rules for L-system.

win.show()