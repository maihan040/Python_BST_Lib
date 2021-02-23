'''
	BST_Lib.py

	Module to define the functions that can be carried out on a binary search tree

	Created: 02/12/2021

	Last Updated: 02/22/2021

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
#   	insert__node                                        					#
#       preorder_print                                                                          #
#       inorder_print                                                                           #
#       postorder_print                                                                         #
#	get_bst_preorder									#
# 	get_bst_inorder										#
# 	get_bst_postorder									#
#                                                                                               #
#################################################################################################

###################################### Inser Function ###########################################
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
def insert_node(BST, val): 

	# check whether the passed BST is empty. In which case all that's needed is to have the 
	# root contain "val" and the method is done with it's job
	if BST.root == None: 
		BST.root = BST_Node.BST_Node(val)
		return

	# helper function to traverse the tree to find the right location where to append the new 
	# value in the tree
	def insert(node, key):

		# base case to indicate the recursion has bottomed out
		# simply create a new BST_Node object and return that to
		# the caller 
		if node == None: 
			return BST_Node.BST_Node(key)

		# recursively check which leaf will be the suited parent for this value 
		elif node.val <= val: 
			node.right = insert(node.right, key)

		# traverse the left side 
		else: 
			node.left = insert(node.left, key)
		
		# return the node which acts that the current "root" during this recursive call
		return node
	
	# call the helper function 
	insert(BST.root, val)

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
# Input parameters: "bst_root" root node of bst tree object indicating the current binary	# 
# 		    search tree             							#
#                                                                   				#
# Output: List object showing the order of the node values, as per the ordering chosen		#
#                                               						#
#################################################################################################
def get_bst_preorder(bst_root):

	#local variables
	order = []

	# helper function that will recursively traverse through the tree per the specified order
	def walk_bst_preorder(node):
		
		# base case
		if node == None: 
			return 
	
		# append the current node to the list  
		order.append(node.val)
		
		# move on to left child 
		walk_bst_preorder(node.left)
		
		# move on to right child 
		walk_bst_preorder(node.right)
	
	# call the recursive helper method 
	walk_bst_preorder(bst_root)

	# return the list 
	return order


def get_bst_inorder(bst_root):

	#local variables 
	order = [] 

	# helper function that will recursively traverse through the tree per the specified order
	def walk_bst_inorder(node):     
	
		# base case 
		if node == None: 
			return 
	
		# move on to left child 
		walk_bst_inorder(node.left)     
	
		# append the current node to the list 
		order.append(node.val) 
	
		# move on to the right child  
		walk_bst_inorder(node.right)

	# call the helper function 
	walk_bst_inorder(bst_root)  
	
	# return the list 
	return order


def get_bst_postorder(bst_root):

	#local variables
	order = [] 

	# helper function that will recursively traverse through the tree per the specified order
	def walk_bst_postorder(node):
		
		# base case
		if node == None: 
			return 
		
		# move on to the left child 
		walk_bst_postorder(node.left)
		
		# move on to the right child 
		walk_bst_postorder(node.right)
		
		# append the current node to the list 
		order.append(node.val)
	
	# call the helper function 
	walk_bst_postorder(bst_root)
	
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
def preorder_print(bst_root):

	#get the "list" object which contains the bst preorder ordering
	bst_tree = get_bst_preorder(bst_root)

	#print the contents of the list 
	for node in bst_tree:
		print(str(node), end=' ')

def inorder_print(bst_root):

	#get the "list" object which contains the bst inorder ordering
	bst_tree = get_bst_inorder(bst_root)

	#print the contents of the list 
	for node in bst_tree:
		print(str(node), end=' ')

def postorder_print(bst_root):

	#get the "list" object which contains the postorder ordering
	bst_tree = get_bst_postorder(bst_root)

	#print the contents of the list 
	for node in bst_tree:
		print(str(node), end=' ')

###################################### Balance Tree #############################################
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
def balance_bst(bst): 

	# validation check 
	if bst == None: 
		print("Tree doesn't contain any nodes")
		return
	
	# local variables 
	bst_inorder = get_bst_inorder(bst.root)
	new_tree = BST.BST()

	# helper function that will recursively split the "bst_inorder" list by 2
	# and append the middle value of each of the half list to the newly created tree
	def build_balanced_tree(root, start_idx, end_idx): 

		
		# base case to have the recursion bottom out. 
		# 1. Ensure the start_idx is always less than the end_idx
		# 2. If indices are the same, then this is the last 
		#    element that needs to be inserted in to the tree

		if start_idx > end_idx:
			return 

		if start_idx == end_idx: 
			insert_node(new_tree, bst_inorder[start_idx]) 
		else:
			# compute the midpoint of the current list and use that value to build the tree
			mid_point = (start_idx + end_idx)//2

			# append the current mid value
			insert_node(new_tree, bst_inorder[mid_point])

			# recursively work on the left half of the list 
			build_balanced_tree(new_tree, start_idx, mid_point - 1)

			# do the same for the right side of the list 
			build_balanced_tree(new_tree, mid_point + 1, end_idx)
		
	
	# call the helper function to get the fun started 
	build_balanced_tree(new_tree, 0, len(bst_inorder) - 1)
	
	# return the new tree
	return new_tree

####################################### Invert Tree #############################################
#                                               						#
# Function to invert the tree. After this function the BST will be a mirror reflection of what	#
# it was before this function was called.							#
#												#
# Input parameters: "BST" BST tree object indicating the binary search tree that is to be       # 
#		    invert									#
#                                            							#
# Output: BST, which will be a new tree object containing the exact same nodes, only now having	#
#         a mirrored structure									#
#                                               						#
#################################################################################################
def invert_tree(bst):

	# validation check 
	if bst == None: 
		print("Tree doesn't contain any nodes")
		return

	# helper function which will swap the child nodes of each respective node 
	def invert(node):

		# base case
		if node == None: 
			return
	
		# proceed in a post order fashion while inverting the children of each node
		invert(node.left)
		invert(node.right)

		# main operation, swap left and right children
		temp = node.left
		node.left = node.right
		node.right = temp
	
	# call the helper function 
	invert(bst.root)

#################################### Min/Max Function ###########################################
#                                               						#
# Function to find the smalles/largest value of nodes that are stored in the tree. Since the 	#
# tree is already sorted, the function is quite simple in that it has to traverse all the way	#
# to the left (starting from the root of the tree) to get the smallest element in the tree, and #
# likewise to the same for the right in order to get the max value. 				#
#												#
# Input parameters: "BST" BST tree object indicating the binary search tree that is to be       # 
#		    processed									#
#                                            							#
# Output: Tuple, containing the min/max values that were found in the tree			#
#                                               						#
#################################################################################################
def min_max(bst):

	# validate the tree
	if bst == None: 
		print("Tree is empty, no floor/ceil can be found")
		return 

	# local variables
	min = bst.root 
	max = bst.root

	# find the min value 
	while min.left != None: 
		min = min.left
	
	# find the max value 
	while max.right != None: 
		max = max.right
	
	# return the floor and ceil values 
	return (min.val, max.val)