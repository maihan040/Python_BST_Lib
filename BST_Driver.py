'''
        BST_Driver.py

        Module to test the function of the BST_Lib.py functions 

	Created: 02/15/2021

        Last Updated: 02/18/2021

	Verison: 1.0
        
        Requires: "BST_Lib.py" and "BST_Node.py" modules 
'''

######################################### Imports ###############################################
#												#
# BST.py: BST tree module which will contain all the individual nodes of the tree               #
# BST_Lib.py: BST library module to have access to all the functions to test 	                #
# BST_Node.py: BST Node used to build the tree                                                  #
#												#
#################################################################################################
import BST
import BST_Lib
import BST_Node

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
# Input parameters: root" BST_Node object indicating the current binary search tree             #
#                        							                #
# Output: None, each function will print its result     					#
#												#
#################################################################################################

def test_insert_function(BST):

        print("Before appending: ")
        print(BST.root.__repr__())
        print()

        # add random numbers to the tree
        BST_Lib.insert_node(BST, 5)
        BST_Lib.insert_node(BST, 4)
        BST_Lib.insert_node(BST, 3)
        BST_Lib.insert_node(BST, 2)
        BST_Lib.insert_node(BST, 1)
        BST_Lib.insert_node(BST, 6)
        BST_Lib.insert_node(BST, 7)
        BST_Lib.insert_node(BST, 8)
        BST_Lib.insert_node(BST, 9)
  
        #print the result again 
        print("After appending: ")
        print(BST.root.__repr__())
        print()

def test_print_functions(BST): 

        # print the tree after all the new elements have been added, as well as testing the other orders
        print("Current tree structure (inorder): " )
        BST_Lib.inorder_print(BST.root)
        print()

        print("Current tree structure after appending elements (preorder): " )
        BST_Lib.preorder_print(BST.root)
        print()

        print("Current tree structure (postorder): " )
        BST_Lib.postorder_print(BST.root)
        print()

def test_balancing_function(BST): 

        print("Current tree structure before balancing: ")
        print(BST.root.__repr__())
        print()
        BST = BST_Lib.balance_bst(BST)
        print("Tree structure after balancing: ")
        print(BST.root.__repr__())
        print()

def test_min_max_function(BST):

        print("Searching tree for min/max values: " )
        min_max = BST_Lib.min_max(BST)
        print("Min: " + str(min_max[0]) + " Max : " + str(min_max[1]))
        print()

def test_invert_function(BST):

        print("Tree order before inverting it: ")
        print(BST.root.__repr__())
        BST_Lib.invert_tree(BST)
        print("Tree structure after inverting: " )
        print(BST.root.__repr__())
        print()

############################################# Main ##############################################

# Create tree 
BST_Tree = BST.BST()

# Test Append Function 
test_insert_function(BST_Tree)

# Test Print Functions 
#test_print_functions(BST_Tree)

# Test the balancing function 
#test_balancing_function(BST_Tree)

# Test min/max FUnction
#test_min_max_function(BST_Tree)

# Test invert tree function 
test_invert_function(BST_Tree)
