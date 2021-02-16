'''
        BST_Driver.py

        Module to test the function of the BST_Lib.py functions 

	Created: 02/15/2021

	Verison: 1.0
'''

######################################### Imports ###############################################
#												#
# BST_Lib.py: BST library module to have access to all the functions to test 	                #
# BST_Node.py: BST Node used to build the tree                                                  #
#												#
#################################################################################################
import BST_Lib as bst
import BST_Node as node

########################################## MAIN #################################################
#												#
# "Main" method of the script. Tests all the possible functions one by one after createing the 	#
# binary search tree                                                                            #
#												#
#################################################################################################

###################################### Test Functions ###########################################
#												#
# Functions which will be used to test each of the designed functions.                          #
#                                                                                               #
#                                                                                               #
# Input parameters: root" BST_Node object indicating the current binary search tree             #
#                        							                #
# Output: None, each function will print its result     					#
#												#
#################################################################################################

def test_append_function(root):

        # add random numbers to the tree
        bst.append_node(root, 3)
        bst.append_node(root, 7)
        bst.append_node(root, 4)
        bst.append_node(root, 2)
        bst.append_node(root, 6)
        bst.append_node(root, 8)
        bst.append_node(root, 9)
        bst.append_node(root, 1)

def test_print_functions(root): 

        # print the tree after all the new elements have been added, as well as testing the other orders
        print("Current tree structure (inorder): " )
        bst.inorder_print(root)
        print()

        print("Current tree structure after appending elements (preorder): " )
        bst.preorder_print(root)
        print()

        print("Current tree structure (postorder): " )
        bst.postorder_print(root)
        print()


############################################# Main ##############################################

# Create tree 
root = node.BST_Node(5)

# Test Append Function 
print("Before appending: ")
print(root.__repr__())
print()

# call the append function 
test_append_function(root)

#print the result again 
print("After appending: ")
print(root.__repr__())
print()

# Test Print Functions 
test_print_functions(root)
print()
