'''
	BST.py

	Module to define the BST class which will be used by the subsequent BST_Lib module

	This is a wrapper class for the BST_Node, so that subsequent methods have greater flexibility
	in working with binary search threes whether they have a root val or not

	Created: 02/18/2021

	Last Updated: 02/18/2021

	Verison: 1.0
'''

######################################### Imports ###############################################
#												#
# BST_Node.py: BST Node used to build the tree                                                  #
#												#
#################################################################################################
import BST_Node

####################################### Class Definition ########################################
#                                                                                       	#
# Notes: Tree will initially contain an empty BST_Node, unless the user specified a value	#
#                                                                                       	#
#       Should the user not supply a data value for the root of the tree, then the value will  	#
#	defaulted (to None) as per the BST_Node class init method				#
#                                                                                       	#
#################################################################################################

class BST:

	# init method. Checks to see whether the user supplied a value for the value 
	# and will take the appropriate action in constructing the node 
	def __init__(self, val = None):

		if val == None: 
			self.root = None
		else: 
			self.root = BST_Node.BST_Node(val)

	
	# debug "__repr__" method to help out for debugging 
	def __repr__(self):

		# delegate the function to the tree's root (BST_Node) instance
		# if the tree contains any nodes
		if isinstance(self.root, BST_Node.BST_Node):
			return self.root.__repr__()
		else: 
			return f"(Tree is empty)"
	