""" 
Change the file knob to end with .mov

super-simple one-liner version:
>>> nuke.selectedNode()["file"].setValue(os.path.splitext(nuke.selectedNode()["file"].value())[0] + ".mov")
"""

import nuke

# Get the file knob
file_knob = nuke.selectedNode().knob("file")

# Get the current file path
current_path = file_knob.value()

# Get the path without extension
root, _ = os.path.splitext(current_path)

# Set the new file path with .mov
file_knob.setValue(root + ".mov")
