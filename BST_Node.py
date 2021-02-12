'''
	BST_Node.py

	module to define the BST node class which will be used by the subsequent BST_Lib module

	created: 02/11/2021

	verison: 1.0
'''

################################## Class Definition #####################################
#                                                                                       #
#Notes: Initially, nodes will have no children which is why the "left" and "right"      #
#       attributes are referring to "None"                                               #
#                                                                                       #
#       Should the user not supply a data value for the "vaL" attribute a "NaN"         #
#       (not a number) will be added by default to indicate that this                   #
#       node doesn't contain a usefull value                                            #
#########################################################################################

class BST_Node:
    
    #
    #define default values that will be used for each instance
    #
    def __init__(self, data = "NaN", left=None, right=None):
        self.val = data
        self.right = right
        self.left = left
    
    #
    #debug "__repr__" method to help out for debugging 
    #
    def __repr__(self):
        return f"(Node val: {self.val})"
