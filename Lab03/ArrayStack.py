class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        print(len(self.data)) 

    def is_empty(self):
        
        if self.data == []:
            print(True)
        else:
            print(False)

    def push(self, input_data):
        return self.data.append(input_data)

    def pop(self):
        if self.data == []:
            print("UnderFlow")
        else:
            
            x = self.data.pop()
            return x

    def stackTop(self):
        if self.data == []:
            print("Underflow")
        else:
            index = self.data[len(self.data)-1]
            print(index)

    def printStack(self):
        print(self.data)

mystack = ArrayStack()
mystack.push(10)
mystack.push(20)
mystack.pop()
