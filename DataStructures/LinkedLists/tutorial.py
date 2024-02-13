from utils import Node, LinkedList

LL = LinkedList()

LL.insertAtBegin(4)
LL.insertAtBegin(2)
LL.insertAtEnd(6)
LL.insertAtEnd(18)

LL.printLL()

LL.insertAtIndex(8, 2)
LL.insertAtEnd(10)
LL.insertAtIndex(8, 4)


LL.printLL()

LL.removeFirstNode()
LL.removeLastNode()

LL.insertAfterData(25, 4)
LL.insertAfterData(1, 18)

LL.printLL()

LL.insertAfterData(35, 25)
LL.printLL()

print(LL.sizeOfLL())

linked = LL.getLinkedListAsList()
print(linked)
print(type(linked))

rev_LL = LL.reverse()
print(rev_LL)