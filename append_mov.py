import nuke

# Get the 'file' knob from the selected node
file_knob = nuke.selectedNode().knob("file")

# Get the current file path from the knob
current_path = file_knob.value()

# Add ".mov" to the end of the current path
new_path = current_path + ".mov"

# Set the new path back to the file knob
file_knob.setValue(new_path)
