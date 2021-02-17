'''
	BST_Lib.py

	Module to define the functions that can be carried out on a binary search tree

	Created: 02/12/2021

	Verison: 1.0

	Requires: "BST_Node.py" module
'''

######################################### Imports ###############################################
#												#
# BST_Node.py: This will be the main module needed in order to build the binary search tree.    #
#												#
#################################################################################################
import BST_Node

####################################### Functions ###############################################
#                                               						#
# BST_Node.py: This will be the main module needed in order to build the binary search tree.    #
#                                               						#
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
# Input parameters: "root" BST_Node object indicating the current binary search tree where user #
# wishes to add a new node "val" (val" the value of the new node that will need to be added to 	#
# the tree tree).    										#
#                                               						#
# Output: None                                          					#
#                                               						#
#################################################################################################
def append_node(root, val): 

	# validation check. Should the tree be emptpy, make this val the root 
	if root == None: 
		root =  BST_Node.BST_Node(val)
		return root

	# recursively check which leaf will be the suited parent for this value 
	if root.val <= val: 
		root.right = append_node(root.right, val)
				
	else: #traverse the left side 
		root.left = append_node(root.left, val)

	# return the root 
	return root

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
# Input parameters: root" BST_Node object indicating the current binary search tree             #
#                                                                   				#
# Output: List object showing the order of the node values, as per the ordering chosen		#
#                                               						#
#################################################################################################
def get_bst_preorder(root):

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
	recurse_preorder(root)

	# return the list 
	return order


def get_bst_inorder(root):

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
	recurse_inorder(root)  
	
	# return the list 
	return order


def get_bst_postorder(root):

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
	recurse_postorder(root)
	
	# return the list 
	return order

##################################### Print Functions ###########################################
#                                               						#
# Printing the ordering of the nodes as per the three possible orderings (preorder, inorder,	#
# and postorder). These functions will call the corresponding "get_bst_<type>order" functions	#
# which perform the core of the logic.								#
#												#
# Input parameters: root" BST_Node object indicating the current binary search tree             #
#                                                         					#
# Output: None, as the functions will simply print the ordering and return			#
#                                               						#
#################################################################################################
def preorder_print(root):

	#get the "list" object which contains the ordering
	bst_tree = get_bst_preorder(root)

	#print the contents of the list 
	for node in bst_tree:
		print(str(node), end=' ')

def inorder_print(root):

	#get the "list" object which contains the ordering
	bst_tree = get_bst_inorder(root)

	#print the contents of the list 
	for node in bst_tree:
		print(str(node), end=' ')

def postorder_print(root):

	#get the "list" object which contains the ordering
	bst_tree = get_bst_postorder(root)

	#print the contents of the list 
	for node in bst_tree:
		print(str(node), end=' ')

#################################### Balance Function ###########################################
#                                               						#
# Function to balance the tree. Ideally you would want the tree to always be fully balanced,	#
# meaning each node has two children (provided there are enough nodes in the tree) as supposed	#
# to a sparse tree. Worst case for example would be to append the tree with all the values in 	#
# either increasing or decreasing order								#
#												#
# Input parameters: root" BST_Node object indicating the current binary search tree             # 
#                                            							#
# Output: BST_Node, which will be the root of the newly (balance) tree that was created		#
#                                               						#
#################################################################################################
def balance_bst(root): 

	# local variables 
	bst_inorder = get_bst_inorder(root)
	new_root = None

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
		append_node(new_root, bst_inorder[mid_point])

		# recursively work on the left half of the list 
		build_balanced_tree(new_root, bst_inorder, start_idx, mid_point - 1)

		# do the same for the right side of the list 
		build_balanced_tree(new_root, bst_inorder, mid_point + 1, end_idx)
	
	# call the helper function to get the fun started 
	build_balanced_tree(new_root, bst_inorder)
	
	# return the new tree
	return new_root