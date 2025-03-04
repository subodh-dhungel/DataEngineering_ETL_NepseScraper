class Stack:
    def __init__(self):
        self.list = []

    #push
    def push(self, elem):
        self.list.append(elem)
        print("pushed element into the stack: "+ str(elem))

    #pop
    def pop(self):
        if not self.isEmpty():
            poppedElem = self.list.pop()
            print("the popped element from the stack : "+ str(poppedElem))
        else:
            print("Stack is empty! Nothing to pop")

    #peek
    def peek(self):
        lastIdx = -1
        lastElem = self.list[lastIdx]
        print("the last element of the stack: "+ str(lastElem))

    #check if the stack is empty
    def isEmpty(self):
        return len(self.list) == 0
    
    def size(self):
        return len(self.list)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
print(stack.peek())
stack.pop()
print(stack.peek())