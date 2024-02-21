class Heap:
    def __init__(self) -> None:
        self.heap = []
    
    def insert(self, data):
        self.heap.append(data)
        self.heapifyup()
        print(self.heap)
        
    def delete(self):
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapifydown()
        print(root)
        
    def heapifyup(self):
        index = len(self.heap) -1
        parent = (index-1)//2
        while index>0:
            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
                parent = (index-1)//2
            else:
                break
    
    def heapifydown(self):
        # index = len(self.heap) -1
        # parent = (index-1)//2
        # while index>0:
        #     if self.heap[index] > self.heap[parent]:
        #         self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
        #         index = parent
        #         parent = (index-1)//2
        #     else:
        #         break
            