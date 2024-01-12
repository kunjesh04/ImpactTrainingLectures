from utils import Stack

stack = Stack(5)

stack.PUSH(5)
stack.PUSH(10)
stack.PUSH(10)
stack.PUSH(10)
stack.PUSH(100000)

stack.printStack()
stack.PUSH(15345678)
stack.PUSH(34567)
stack.POP()
stack.printStack()

revStack = stack.ReverseStack()
print(revStack)

stack.printStack()


print(type(stack))

print(stack.top)