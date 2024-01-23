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