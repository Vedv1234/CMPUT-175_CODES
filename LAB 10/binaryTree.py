"""
Author: Ved Vyas
Co-Author / Exercise provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)
Resources provided by: University of Alberta CMPUT 175 Course Team & Instructors (2023)

Functionality of code: 
In this lab, I've implemented a binary tree data structure and various tree traversal algorithms. 
The code includes methods for creating and manipulating binary trees, finding minimum and maximum values, 
and even reconstructing a binary tree from its inorder and preorder traversals. What I found really cool 
about this project is how it helped me understand recursive algorithms better, especially when dealing 
with tree structures. The visualization part using ASCII art was particularly interesting as it lets me 
actually see the tree structure I'm working with.
"""

class BinaryTree:
    def __init__(self, rootElement):
        # I'm initializing my binary tree with a root element and setting both children to None initially
        self.key = rootElement 
        self.left = None
        self.right = None
        
    '''My getter methods to access tree node properties'''
    def getLeft(self):
        # I'm returning the left child of the current node
        return self.left
    
    def getRight(self):
        # I'm returning the right child of the current node
        return self.right
    
    def getKey(self):
        # I'm returning the key value stored in the current node
        return self.key
    
    '''My setter methods to modify tree node properties'''
    def setKey(self, key):
        # I'm updating the key value of the current node
        self.key = key
        
    def setLeft(self, left):
        # I'm setting the left child of the current node
        self.left = left        
  
    def setRight(self, right):
        # I'm setting the right child of the current node
        self.right = right
        
    def insertLeft(self, newNode):
        # Here I'm inserting a new node as the left child, preserving any existing left subtree
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.left = self.left
            self.left = t
  
    def insertRight(self, newNode):
        # Similarly, I'm inserting a new node as the right child, preserving any existing right subtree
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.right = self.right
            self.right = t 
            
    def _strHelper(self):
        # This is my helper method for creating a string representation of the tree
        # It returns a list of strings, the total width, middle position, and height
        
        # My base case: when I have a leaf node
        if self.getLeft() == None and self.getRight() == None:
            row = '%s' % self.key
            width = len(row)
            middle = width // 2
            height = 1
            return [row], width, middle, height 

        keyStr = '%s' % self.key
        keyStrLength = len(keyStr)
        
        # I'm handling the case where I only have a left child
        if self.getLeft() != None and self.getRight() == None:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength) * ' '
            shiftedRows = [row + keyStrLength * ' ' for row in leftRows]
            return [firstRow, secondRow] + shiftedRows, leftWidth + keyStrLength, leftWidth + keyStrLength // 2, leftHeight + 2

        # I'm handling the case where I only have a right child
        elif self.getLeft() == None and self.getRight() != None:
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper()
            firstRow = keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = (keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            shiftedRows = [keyStrLength * ' ' + row for row in rightRows]
            return [firstRow, secondRow] + shiftedRows, rightWidth + keyStrLength, keyStrLength // 2, rightHeight + 2

        # Here I'm handling the case where I have both children
        else:
            leftRows, leftWidth, leftMiddle, leftHeight = self.getLeft()._strHelper()
            rightRows, rightWidth, rightMiddle, rightHeight = self.getRight()._strHelper()
            
            firstRow = (leftMiddle + 1) * ' ' + (leftWidth - leftMiddle - 1) * '_' + keyStr + rightMiddle * '_' + (rightWidth - rightMiddle) * ' '
            secondRow = leftMiddle * ' ' + '/' + (leftWidth - leftMiddle - 1 + keyStrLength + rightMiddle) * ' ' + '\\' + (rightWidth - rightMiddle - 1) * ' '
            
            # I'm making sure both subtrees appear at the same height by adding padding
            if leftHeight < rightHeight:
                leftRows += [leftWidth * ' '] * (rightHeight - leftHeight)
            else:
                rightRows += [rightWidth * ' '] * (leftHeight - rightHeight)
            pairedRows = zip(leftRows, rightRows)
            rows = [firstRow, secondRow] + [i + keyStrLength * ' ' + j for i, j in pairedRows]
            return rows, leftWidth + rightWidth + keyStrLength, leftWidth + keyStrLength // 2, max(leftHeight, rightHeight) + 2
    
    def __str__(self):
        # I'm creating a string representation of my tree for visualization
        rows, _, _, _ = self._strHelper()
        result = ''
        for row in rows:
            result += row + "\n"
        return result

################################################################################
##  EXERCISE 1 - My implementation of tree traversal algorithms
################################################################################    

def preorder(tree):
    '''
    I'm implementing a preorder traversal that visits the root, then left subtree, then right subtree
    '''
    if tree is not None:
        print(tree.getKey(), end=" ")  # First I print the current node
        preorder(tree.getLeft())       # Then I recursively traverse the left subtree
        preorder(tree.getRight())      # Finally I recursively traverse the right subtree
            
def inorder(tree):
    '''
    I'm implementing an inorder traversal that visits the left subtree, then root, then right subtree
    '''
    if tree is not None:
        inorder(tree.getLeft())        # First I traverse the left subtree
        print(tree.getKey(), end=" ")  # Then I print the current node
        inorder(tree.getRight())       # Finally I traverse the right subtree
    
def postorder(tree):
    '''
    I'm implementing a postorder traversal that visits the left subtree, then right subtree, then root
    '''
    if tree is not None:
        postorder(tree.getLeft())      # First I traverse the left subtree
        postorder(tree.getRight())     # Then I traverse the right subtree
        print(tree.getKey(), end=" ")  # Finally I print the current node

################################################################################
##  EXERCISE 2 - My implementation of min/max finding algorithms
################################################################################

def findMinKey(tree):
    '''
    I'm implementing a function to find the minimum value in the binary tree
    '''
    if tree is None:
        return None
    elif tree.getLeft() is None:  # If there's no left child, I've found the minimum
        return tree.getKey()
    else:
        return findMinKey(tree.getLeft())  # I keep going left until I can't anymore
    
def findMaxKey(tree):
    '''
    I'm implementing a function to find the maximum value in the binary tree
    '''
    if tree is None:
        return None
    elif tree.getRight() is None:  # If there's no right child, I've found the maximum
        return tree.getKey()
    else:
        return findMaxKey(tree.getRight())  # I keep going right until I can't anymore

################################################################################
##  EXERCISE 3 - My implementation of tree construction from traversals
################################################################################

def buildTree(inOrder, preOrder):
    '''
    I'm implementing a function to reconstruct a binary tree from its inorder and preorder traversals
    '''
    if not inOrder or not preOrder:
        return None
    
    root_val = preOrder[0]  # I know the first element in preOrder is always the root
    root = BinaryTree(root_val)
    
    # I'm finding where the root appears in the inorder traversal
    root_index = inOrder.index(root_val)
    
    # I'm recursively building the left and right subtrees
    # Everything before root_index in inOrder is in the left subtree
    root.setLeft(buildTree(inOrder[:root_index], preOrder[1:root_index + 1]))
    # Everything after root_index in inOrder is in the right subtree
    root.setRight(buildTree(inOrder[root_index + 1:], preOrder[root_index + 1:]))
    
    return root

################################################################################
##  My main function to test all the implementations
################################################################################

def main():
    # I'm creating a test tree to verify all my implementations
    tree = BinaryTree(1)
    tree.insertLeft(2)
    tree.insertRight(7)
    tree.getLeft().insertLeft(3)
    tree.getLeft().insertRight(6)
    tree.getLeft().getLeft().insertLeft(4)
    tree.getLeft().getLeft().insertRight(5)
    tree.getRight().insertLeft(8)
    tree.getRight().insertRight(9)

    print("the tree:\n")
    print(tree)
    
    # Testing my traversal methods
    print("preorder traversal:")
    preorder(tree)
    print()
    print("inorder traversal:")
    inorder(tree)
    print()
    print("postorder traversal:")
    postorder(tree)
    print()

    # Testing my min/max finding methods
    print('Max value in tree:', findMaxKey(tree))
    print('Min value in tree:', findMinKey(tree))

    # Testing my tree construction method with two different examples
    inor = [4,3,5,2,6,1,8,7,9]
    preor = [1,2,3,4,5,6,7,8,9]
    theTree = buildTree(inor,preor)
    print(theTree)
    
    inor2 = [3,2,4,1,5]
    preor2 = [1,2,3,4,5]
    theTree2 = buildTree(inor2,preor2)
    print(theTree2)

if __name__ == "__main__":
    main()

# I'm importing openpyxl to check its version
import openpyxl as xl
print(xl.__version__)