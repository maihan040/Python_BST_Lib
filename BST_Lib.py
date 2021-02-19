'''
	BST_Lib.py

	Module to define the functions that can be carried out on a binary search tree

	Created: 02/12/2021

	Last Updated: 02/18/2021

	Verison: 1.0

	Requires: "BST_Node.py" module
'''

######################################### Imports ###############################################
#												#
# BST.py: This will be the core module needed in order to build the binary search tree.		#
#												#
#################################################################################################
import BST
import BST_Node

####################################### Functions ###############################################
#                                               						#
# Following functions are defined below:                            				#
#   	append__node                                        					#
#       preorder_print                                                                          #
#       inorder_print                                                                           #
#       postorder_print                                                                         #
#	get_bst_preorder									#
# 	get_bst_inorder										#
# 	get_bst_postorder									#
#                                                                                               #
#################################################################################################

##################################### Append Function ###########################################
#                                               						#
# Append function. This will add a new element to the tree in the corresponding order       	#
#                                               						#
# Binary search trees have the characteristic of the left child always being less than      	#
# or equal to the current node (the parent) value, and the right child being greater        	#
# than the parent                                       					#
#                                               						#  	 
# Input parameters: "BST" BST object indicating the current binary search tree where user wants #
# to add a new node "val" (val being the value of the new node that will need to be added to 	#
# the tree).    										#
#                                               						#
# Output: None                                          					#
#                                               						#
#################################################################################################
def append_node(BST, val): 

	# check whether the passed BST has any nodes
	if BST.root == None: 
		BST.root = BST_Node.BST_Node(val)
		return

	# helper function to traverse the tree to find the right location where to append the new 
	# value in the tree
	def find_leaf_to_append_node(node):

		# base case to indicate the recursion has bottomed out
		if node == None: 
			return BST_Node.BST_Node(val)

		# recursively check which leaf will be the suited parent for this value 
		if node.val <= val: 
			node.right = find_leaf_to_append_node(node.right)

		else: #traverse the left side 
			node.left = find_leaf_to_append_node(node.left)
	
	# call the helper function 
	find_leaf_to_append_node(BST.root)

##################################### Order Functions ###########################################
#                                               						#
# Binary trees can have three different orders to represents the ordering of the nodes, 	#
# consisting of each parent node along the values of each of their children. 			#
#												#
# The ordering can be as follows:                   						#
#                                                                                               #
#       Inorder   - left child node value, parent node value, and right child node value        #
#       Preorder  - parent node value, left child node value, and right child node value        #
#       Postorder - left child node value, right child node value, and parent node value        #
#                                                                                               #
#       These functions work by recursively calling themselves in determining the next node     #
#                                                                                               #
# Input parameters: "BST" bst tree object indicating the current binary search tree             #
#                                                                   				#
# Output: List object showing the order of the node values, as per the ordering chosen		#
#                                               						#
#################################################################################################
def get_bst_preorder(BST):

	#local variables
	order = []

	# helper function that will recursively traverse through the tree per the specified order
	def recurse_preorder(node):
		
		# base case
		if node == None: 
			return 
	
		# append the current node to the list  
		order.append(node.val)
		
		# move on to left child 
		recurse_preorder(node.left)
		
		# move on to right child 
		recurse_preorder(node.right)
	
	# call the recursive helper method 
	recurse_preorder(BST.root)

	# return the list 
	return order


def get_bst_inorder(BST):

	#local variables 
	order = [] 

	# helper function that will recursively traverse through the tree per the specified order
	def recurse_inorder(node):     
	
		# base case 
		if node == None: 
			return 
	
		# move on to left child 
		recurse_inorder(node.left)     
	
		# append the current node to the list 
		order.append(node.val) 
	
		# move on to the right child  
		recurse_inorder(node.right)

	# call the helper function 
	recurse_inorder(BST.root)  
	
	# return the list 
	return order


def get_bst_postorder(BST):

	#local variables
	order = [] 

	# helper function that will recursively traverse through the tree per the specified order
	def recurse_postorder(node):
		
		# base case
		if node == None: 
			return 
		
		# move on to the left child 
		recurse_postorder(node.left)
		
		# move on to the right child 
		recurse_postorder(node.right)
		
		# append the current node to the list 
		order.append(node.val)
	
	# call the helper function 
	recurse_postorder(BST.root)
	
	# return the list 
	return order

##################################### Print Functions ###########################################
#                                               						#
# Printing the ordering of the nodes as per the three possible orderings (preorder, inorder,	#
# and postorder). These functions will call the corresponding "get_bst_<type>order" functions	#
# which perform the core of the logic.								#
#												#
# Input parameters: "BST" BST tree object indicating the binary search tree to be printed       #
#                                                         					#
# Output: None, as the functions will simply print the ordering and return			#
#                                               						#
#################################################################################################
def preorder_print(BST):

	#get the "list" object which contains the ordering
	bst_tree = get_bst_preorder(BST)

	#print the contents of the list 
	for node in bst_tree:
		print(str(node), end=' ')

def inorder_print(BST):

	#get the "list" object which contains the ordering
	bst_tree = get_bst_inorder(BST.root)

	#print the contents of the list 
	for node in bst_tree:
		print(str(node), end=' ')

def postorder_print(BST):

	#get the "list" object which contains the ordering
	bst_tree = get_bst_postorder(BST.root)

	#print the contents of the list 
	for node in bst_tree:
		print(str(node), end=' ')

#################################### Balance Function ###########################################
#                                               						#
# Function to balance the tree. Ideally you would want the tree to always be fully balanced,	#
# meaning each node has ideally two children (provided there are enough nodes in the tree to	#
# make this possible) as supposed to a sparse tree. Worst case for example would be to append	#
# the tree with all the values in either increasing or decreasing order				#
#												#
# Input parameters: "BST" BST tree object indicating the binary search tree that is to be       # 
#		    balanced									#
#                                            							#
# Output: BST, which will be a new tree object containing the exact same nodes, only now being	#
#	  balanced										#
#                                               						#
#################################################################################################
def balance_bst(BST): 

	# local variables 
	bst_inorder = get_bst_inorder(BST.root)
	new_tree = None

	# helper function that will recursively split the "bst_inorder" list by 2
	# and append the middle value of each of the half list to the newly created tree
	def build_balanced_tree(root, bst_inorder, start_idx = 0, end_idx = len(bst_inorder) - 1): 

		# base case to have the recursion bottom out. Once this point has been reached 
		# then there is nothing left to further process 
		if start_idx == end_idx: 
			return 

		# compute the midpoint of the current list and use that value to build the tree
		mid_point = (start_idx + end_idx)//2

		# append the current mid value
		append_node(new_tree, bst_inorder[mid_point])

		# recursively work on the left half of the list 
		build_balanced_tree(new_tree, bst_inorder, start_idx, mid_point - 1)

		# do the same for the right side of the list 
		build_balanced_tree(new_tree, bst_inorder, mid_point + 1, end_idx)
	
	# call the helper function to get the fun started 
	build_balanced_tree(new_tree, bst_inorder)
	
	# return the new tree
	return new_tree