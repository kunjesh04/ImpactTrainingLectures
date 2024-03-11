class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None
        
    def printInorder(self, node):
        '''
        Prints the Tree in Inorder method (Left, ROOT, Right)
        '''
        if node:
            self.printInorder(node.left)
            print(node.data, end=" ")
            self.printInorder(node.right)            

    
    def insertLeft(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return
        else:
            temp = self.root
            while temp.left != None:
                temp = temp.left
            temp.left = newNode
            return
    
    def insertRight(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
            return
        else:
            temp = self.root
            while temp.right != None:
                temp = temp.right
            temp.right = newNode
            return

class BinarySearchTree:
    
    def __init__(self):
        self.root = None
    
    def printInorder(self, node):
        '''
        Prints the Tree in Inorder method (Left, ROOT, Right)
        '''
        if node:
            self.printInorder(node.left)
            print(node.data, end=" ")
            self.printInorder(node.right)
        
    
    def insert(self, data):
        self.root = self.insert_recursive(self.root, data)
    
    def insert_recursive(self, current, data):
        # newNode = Node(data)
        if current is None:
            return Node(data)
        
        if data < current.data:
            current.left = self.insert_recursive(current.left, data)
        elif data > current.data:
            current.right = self.insert_recursive(current.right, data)
        
        return current
    
    def checkDataIn(self, current, data):
        if current is None:
            return False
        if data == current.data:
            return True
        elif data < current.data:
            return self.checkDataIn(current.left, data)
        elif data > current.data:
            return self.checkDataIn(current.right, data)        

    def isInTree(self, data):
        current = self.root
        is_present = self.checkDataIn(current, data)
        return is_present

    def deleteNode(self, current, key):
        if current is None:
            return current
        
        # Deletion of Leaf Node
        if current.data > key:
            current.left = self.deleteNode(current.left, key)
            return current
        elif current.data < key:
            current.right = self.deleteNode(current.right, key)
            return current
        
        # Deletion of node whose one children is empty
        if current.left is None:
            temp = current.right
            del current
            return temp
        elif current.right is None:
            temp = current.left
            del current
            return temp


# Generic tree node class 
class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
  
# AVL tree class which supports the  
# Insert operation 
class AVL_Tree(object): 
  
    # Recursive function to insert key in  
    # subtree rooted with node and returns 
    # new root of subtree. 
    def insert(self, root, key): 
      
        # Step 1 - Perform normal BST 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
  
        # Step 2 - Update the height of the  
        # ancestor node 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        # Step 3 - Get the balance factor 
        balance = self.getBalance(root) 
  
        # Step 4 - If the node is unbalanced,  
        # then try out the 4 cases 
        # Case 1 - Left Left 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
  
        # Case 2 - Right Right 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
  
        # Case 3 - Left Right 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
  
        # Case 4 - Right Left 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
        if not root: 
            return 0
  
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
  
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
  
  
# Driver program to test above function 

  
# This code is contributed by Ajitesh Pathak