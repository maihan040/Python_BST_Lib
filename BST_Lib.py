'''
	BST_Lib.py

	Module to define the main functions that can be carried out on a binary search tree

	Created: 02/12/2021

	Verison: 1.0

	Requires: "BST_Node.py" module
'''

######################################### Imports ###############################################
#																								#
# BST_Node.py: This will be the main module needed in order to build the binary search tree.	#
# 																								#
#################################################################################################
import BST_Node

####################################### Functions ###############################################
#																								#
# BST_Node.py: This will be the main module needed in order to build the binary search tree.	#
#																								#
#																								#
# Following functions are defined below:														#
#																								#
#################################################################################################

##################################### Append Function ###########################################
#																								#
# Append function. This will add a new element to the tree in the corresponding order			#
# 																								#
# Binary search trees have the characteristic of the left child always being less than			#
# or equal to the current node (the parent) value, and the right child being greater			#
# than the parent																				#
#																								#	
# Input parameters: "root" which is the root of the current binary search tree where user		#
# wishes to add a new node "val" 																#
# 		"val" the value of the new node that will need to be added to the tree tree.			#
# 																								#
# Output: None																					#
#																								#
#################################################################################################
def append_bst(root, val): 

	#validation check 
	if root == None: 
		return BST_Node.Node(val) 

	#recursively check which leaf will be the suited parent for this value 
	if root.val <= val: 
		root.right = append_bst(root.right, val)
	else: #traverse the left side 
		root.left = append_bst(root.left, val)

	#return the root 
	return root
