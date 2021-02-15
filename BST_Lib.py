'''
	BST_Lib.py

	Module to define the functions that can be carried out on a binary search tree

	Created: 02/12/2021

	Verison: 1.0

	Requires: "BST_Node.py" module
'''

######################################### Imports ###############################################
#												#
# BST_Node.py: This will be the main module needed in order to build the binary search tree.	#
#												#
#################################################################################################
import BST_Node

####################################### Functions ###############################################
#												#
# BST_Node.py: This will be the main module needed in order to build the binary search tree.	#
#												#
#												#
# Following functions are defined below:							#
#	append__node    									#
#       preorder_print                                                                          #
#       inorder_print                                                                           #
#       postorder_print                                                                         #
#                                                                                               #
#################################################################################################

##################################### Append Function ###########################################
#												#
# Append function. This will add a new element to the tree in the corresponding order		#
# 												#
# Binary search trees have the characteristic of the left child always being less than		#
# or equal to the current node (the parent) value, and the right child being greater		#
# than the parent										#
#												#	
# Input parameters: "root" BST_Node object indicating the current binary search tree where user	#
# wishes to add a new node "val" 								#
# 		"val" the value of the new node that will need to be added to the tree tree.	#
# 												#
# Output: None											#
#												#
#################################################################################################
def append_node(root, val): 

	#validation check 
	if root == None: 
		return BST_Node.Node(val) 

	#recursively check which leaf will be the suited parent for this value 
	if root.val <= val: 
		root.right = append_node(root.right, val)
	else: #traverse the left side 
		root.left = append_node(root.left, val)

	#return the root 
	return root

##################################### Print Functions ###########################################
#												#
# Binary trees can be printed in three different ways that print the values of each parent node #
# along the values of each of their children. The ordering can be as follows:                   #
#                                                                                               #
#       Inorder   - left child node value, parent node value, and right child node value        #
#       Preorder  - parent node value, left child node value, and right child node value        #
#       Postorder - left child node value, right child node value, and parent node value        #
#                                                                                               #
#       These functions work by recursively calling themselves in determining the next node     #
#                                                                                               #
# Input parameters: root" BST_Node object indicating the current binary search tree             #
#                        							                #
# Output: String object showing the order of the node values					#
#												#
#################################################################################################
def preorder_print(root):

        #local variables
        result = []

        #helper function that will recursively traverse through the tree
        def recurse_preorder(node):

                #base case
	        if node == None: 
	                return 
        
	        #add the current node to the "results" list 
	        result.append(node.val)

	        #move on to left child 
	        recurse_preorder(root.left)

	        #move on to right child 
	        recurse_preorder(root.right)
        
        #call the recursive helper method 
        recurse_preorder(root)

        #return the result 
        return result


def inorder_print(root):

        #local variables 
        result = []

        #helper function that will recursively traverse through the tree
        def recurse_inorder(node):

	        #base case 
	        if node == None: 
	        	return 

	        #move on to left child 
	        recurse_inorder(node.left)

	        #add the current node to the "results" list
	        result.append(node.val)

	        #move on to the right child  
	        recurse_inorder(node.right)
        
        #call the helper function 
        recurse_inorder(root)

        #return the result 
        return result


def postorder_print(root):

        #local variables 
        result = [] 

        #helper function that will recursively traverse through the tree
        def recurse_postorder(node):

	        #base case
	        if node == None: 
	        	return 

	        #move on to the left child 
	        recurse_postorder(node.left)

	        #move on to the right child 
	        recurse_postorder(node.right)

	        #add the current node to the "results" list
	        result.append(node.val)
        
        #call the helper function 
        recurse_postorder(root)

        #return the result 
        return result