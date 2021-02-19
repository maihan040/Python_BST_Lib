'''
	BST_Node.py

	Module to define the BST node class which will be used by the subsequent BST module

    This is the core element class whose instances will be used to build the tree

	Created: 02/11/2021

	Verison: 1.0
'''

################################## Class Definition #####################################
#                                                                                       #
# Notes: Initially, nodes will have no children which is why the "left" and "right"     #
#       attributes are referring to "None"                                              #
#                                                                                       #
#       Should the user not supply a data value for the "vaL" attribute, then that      #
#       value will default to "None" indicating that this node doesn't currently        #
#       contain a useful value                                                          #
#                                                                                       #
#########################################################################################

class BST_Node:
    
    # define default values that will be used for each instance
    def __init__(self, data = None, left=None, right=None):
        self.val = data
        self.right = right
        self.left = left
    
    # debug "__repr__" method to help out for debugging 
    def __repr__(self):
        return f"(Node val: {self.val}, Left child: {self.left}, Right child: {self.right})"
