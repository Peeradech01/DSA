
class ArrayStack:
    def __init__(self):
        self.data = []

    def size(self):
        print(len(self.data)) 

    def is_empty(self):
        
        if self.data == []:
            return True
        else:
            return False

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
    def  is_parentheses_matching(self, expression): # 4.1
        my_list = ArrayStack()
        underflow = False
        for i in expression: # (((A-B)*C)
            if i == '(':
                my_list.push(i)
            elif i == ')':
                if not my_list.is_empty():
                    my_list.pop()
                else:
                    underflow = True
                    print("Underflow")
                    break
        if not my_list.is_empty() or underflow:
            print({"Unmatch"})
        else:
            print(True)


    def copyStack(s1, s2): # 4.2
        s3 = ArrayStack()
        s2.data.clear()
        while not s1.is_empty():
            x = s1.pop()
            s3.push(x)
        while not s3.is_empty():
            x = s3.pop()
            s1.push(x)
            s2.push(x)
        return s1, s2


    def infixToPostfix(self, exp): # 4.3
        return


# mystack = ArrayStack()
# mystack.push(10)
# # mystack.push(20)
# # mystack.push(30)
# s1 = ArrayStack(); s1.push(10); s1.push(20); s1.push(30)
# s2 = ArrayStack(); s2.push(15)
# mystack.copyStack(s1, s2)
# s1.printStack()
# s2.printStack()

#mystack.is_parentheses_matching("(((A-B)*C)))))")

#mystack.printStack()



def copyStack(s1, s2): # 4.2
        s3 = ArrayStack()
        s2.data.clear()
        while not s1.is_empty():
            x = s1.pop()
            s3.push(x)
        while not s3.is_empty():
            x = s3.pop()
            s1.push(x)
            s2.push(x)
        return s1, s2
s1 = ArrayStack(); s1.push(10); s1.push(20); s1.push(30)
s2 = ArrayStack(); s2.push(15)
copyStack(s1, s2)
s1.printStack()
s2.printStack()




def  is_parentheses_matching(expression): # 4.1
        my_list = ArrayStack()
        underflow = False
        for i in expression: # (((A-B)*C)
            if i == '(':
                my_list.push(i)
            elif i == ')':
                if not my_list.is_empty():
                    my_list.pop()
                else:
                    underflow = True
                    print("Underflow")
                    break
        if not my_list.is_empty() or underflow:
            print({"Unmatch"})
        else:
            print(True)

is_parentheses_matching("(A+B)) + (C*D) ")