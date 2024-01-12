class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1
    
    def printStack(self):
        i = 0
        while i<=self.top:
            print(self.stack[i], end=' ')
            i += 1
        print('\n')
            
    def PUSH(self, data):
        if self.top == self.size:
            print('Overflow Condition : Stack is Full')
            return
        self.stack.append(data)
        self.top = self.stack.index(data)
    
    def POP(self):
        if self.top == -1:
            print('Underflow Condition : Stack is Empty')
            return
        self.stack.remove(self.stack[self.top])
        self.top -= 1
    
    def ReverseStack(self):
        st1 = Stack(size=self.size)
        st1 = self.stack[::-1]
        return st1
    
