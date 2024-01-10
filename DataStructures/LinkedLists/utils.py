class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def printLL(self):
        curr_node = self.head
        while(curr_node):
            print(curr_node.data, end=' ')
            curr_node = curr_node.next
        print('\n')
        
    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while (curr_node.next):
            curr_node = curr_node.next
        curr_node.next = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        curr_node = self.head
        position = 0
        
        if position == index:
            self.insertAtBegin(data)
        else:
            while(curr_node != None and position+1 != index):
                position += 1
                curr_node = curr_node.next
            
            if curr_node.next != None:
                new_node.next = curr_node.next
                curr_node.next = new_node
            else:
                print('Index Not Present')
            
    def removeFirstNode(self):
        if self.head == None:
            return
        self.head = self.head.next
    
    def removeLastNode(self):
        if self.head is None:
            return
        curr_node = self.head
        while (curr_node.next.next):
            curr_node = curr_node.next
        
        curr_node.next = None    