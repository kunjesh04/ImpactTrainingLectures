from utils import Node, LinkedList

LL = LinkedList()

LL.insertAtBegin(4)
LL.insertAtBegin(2)
LL.insertAtEnd(6)

LL.printLL()

LL.insertAtIndex(8, 2)
LL.insertAtEnd(10)

LL.printLL()

LL.removeFirstNode()
LL.removeLastNode()

LL.printLL()