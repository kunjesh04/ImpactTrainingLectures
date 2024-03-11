from utils import *

# tree = Tree()

# nodes = int(input('Enter number of nodes to enter'))

# for i in range(nodes):
#     dt = int(input('Enter Data'))
#     side = input('Enter Side [L/R] : ')
#     if side=='L':
#         tree.insertLeft(dt)
#     elif side=='R':
#         tree.insertRight(dt)
#     else:
#         print('Enter side from options only')

# tree.printInorder(tree.root)

# bst = BinarySearchTree()

# bst.insert(10)
# bst.insert(15)
# bst.insert(5)
# bst.insert(25)
# bst.insert(20)

# print('Inorder Traversal of Tree : ')
# bst.printInorder(bst.root)
# print('')

# presence_of_25 = bst.isInTree(25)
# if presence_of_25:
#     print('25 is present')
# else:
#     print('25 is absent')

# presence_of_1000 = bst.isInTree(1000)
# if presence_of_1000:
#     print('1000 is present')
# else:
#     print('1000 is absent')

# del_data = bst.deleteNode(bst.root, 25)
# print('Tree After Deletion : ')
# bst.printInorder(bst.root)
# print('')

# avl = AVLTree()

# avl.insert(data=9)
# avl.insert(data=3)
# avl.insert(data=15)
# avl.insert(data=17)
# avl.insert(5)
# avl.insert(20)
# avl.insert(25)
# avl.printDetailsOf(avl.root)

myTree = AVL_Tree() 
root = None
  
root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25) 
  
"""The constructed AVL Tree would be 
            30 
           /  \ 
         20   40 
        /  \     \ 
       10  25    50"""
  
# Preorder Traversal 
print("Preorder traversal of the", 
      "constructed AVL tree is") 
myTree.preOrder(root) 
print() 