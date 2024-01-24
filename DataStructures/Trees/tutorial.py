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

print('Inorder Traversal of Tree : ')
bst.printInorder(bst.root)
print('')

presence_of_25 = bst.isInTree(25)
if presence_of_25:
    print('25 is present')
else:
    print('25 is absent')

presence_of_1000 = bst.isInTree(1000)
if presence_of_1000:
    print('1000 is present')
else:
    print('1000 is absent')

del_data = bst.deleteNode(bst.root, 25)
print('Tree After Deletion : ')
bst.printInorder(bst.root)
print('')

