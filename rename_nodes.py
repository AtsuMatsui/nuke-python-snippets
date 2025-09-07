import nuke

# Rename all selected nodes in order from top to bottom:
# Each node will be named "Bee1", "Bee2", "Bee3", etc.
for i, node in enumerate(nuke.selectedNodes(), start = 1):
    node.setName("Bee{}".format(i))