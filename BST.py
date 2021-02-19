'''
	BST.py

	Module to define the BST class which will be used by the subsequent BST_Lib module

	This is a wrapper class for the BST_Node, so that subsequent methods have greater flexibility
	in working with binary search threes whether they have a root val or not

	Created: 02/18/2021

	Verison: 1.0
'''

######################################### Imports ###############################################
#												#
# BST_Node.py: BST Node used to build the tree                                                  #
#												#
#################################################################################################
import BST_Node as node

####################################### Class Definition ########################################
#                                                                                       	#
# Notes: Tree will initially contain an empty BST_Node, unless the user specified a value	#
#                                                                                       	#
#       Should the user not supply a data value for the root of the tree, then the value will  	#
#	defaulted (to None) as per the BST_Node class init method				#
#                                                                                       	#
#################################################################################################

class BST:

	# no arg init method  
	def __init__(self):
		root = node.BST_Node()

	# init method with user supplied value for the root of the tree	
	def __init__(self, val):
		root = node.BST_Node(val)
	
	# repr() method for debuging. Passing this on to the BST_Node repr() method
	def __repr__(self):
		self.root.repr()
