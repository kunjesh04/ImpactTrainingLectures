from utils import Node, Tree, BinarySearchTree

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

bst = BinarySearchTree()

bst.insert(10)
bst.insert(15)
bst.insert(5)
bst.insert(25)
bst.insert(20)

bst.printInorder(bst.root)
