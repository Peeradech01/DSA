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


    
    """Lab04"""
    def  is_parentheses_matching(ex): #4.1
        
        
        list1 = []
        for i in ex:
            if i == "(":
                ex.pop("(")




    def copyStack(s1, s2): #4.2
        check = ArrayStack()
        s2.data.clear()
        for i in s1:
            check.push(i)
        for i in check:
            s2.push(i)
    
        return s1 , s2



s1 = ArrayStack()
s1.push(10)
s1.push(20)
s1.push(30)
s2 = ArrayStack()
s2.push(15)
s1.copyStack(s1,s2)