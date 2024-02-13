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
    
    def insertAfterData(self, ins_data, after_data):
        new_node = Node(ins_data)
        curr_node = self.head
        while(curr_node != None and curr_node.data != after_data):
            curr_node = curr_node.next
        
        if curr_node is None:  # Target data not found
            print('Data Not Present')
            return
        
        new_node.next = curr_node.next
        curr_node.next = new_node
    
            
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
    
    def removeNodeIndex(self, index):
        if self.head == None:
            return
        
        curr_node = self.head
        position = 0
        
        if position == index:
            self.removeFirstNode()
        else:
            while(curr_node != None and position+1 != index):
                position += 1
                curr_node = curr_node.next
            
            if curr_node.next != None:
                curr_node.next = curr_node.next.next
            else:
                print('Index Not Present')
                
    def sizeOfLL(self):
        count = 0
        if self.head == None:
            return count 
        curr_node = self.head
        while (curr_node.next):
            count += 1
            curr_node = curr_node.next
        count += 1 # For last node
        return count
    
    def getLinkedListAsList(self):
        llist = []
        curr_node = self.head
        while curr_node.next:
            llist.append(curr_node.data)
            curr_node = curr_node.next
        return llist
    
    def reverse(self):
        prev=None
        next=None
        curr=self.head
        while(curr):
            next=curr.next
            curr.next=prev
            prev = curr
            curr = next
        return prev

    