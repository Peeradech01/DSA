"""Lab03"""

class ArrayStack:
    """ArrayStack"""    
    def __init__(self):
        self.data = []

    def size(self):
        return (len(self.data)) 

    def is_empty(self):
        if self.data == []:
            return True
        else:
            return False

    def push(self, input_data):
        return self.data.append(input_data)

    def pop(self):
        if self.data == []:
            return "UnderFlow"
        else:
            x = self.data.pop()
            return x

    def stackTop(self):
        if self.data == []:
            return "Underflow"
        else:
            index = self.data[-1]
            return index

    def printStack(self):
        print(self.data)


# mystack = ArrayStack(); mystack.push(10); mystack.push(20); mystack.push(30)
# mystack.size()
# mystack.pop()
# mystack.printStack()




"""Lab04"""

def  is_parentheses_matching(exp): # 4.1
        my_list = ArrayStack()
        underflow = False
        for i in exp: # (((A-B)*C)
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

# is_parentheses_matching("(A+B)) + (C*D)")


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

# s1 = ArrayStack(); s1.push(10); s1.push(20); s1.push(30)
# s2 = ArrayStack(); s2.push(15)
# copyStack(s1, s2)
# s1.printStack()
# s2.printStack()


def infixToPostfix(exp): # 4.3
    stack_p = ArrayStack()
    result = ""

    for i in exp:
        if (i == "*" or i == "/"):
            stack_p.push(i)
        elif i == "-" or i == "+":
            while not stack_p.is_empty(): 
                x = stack_p.pop()
                result += x
            stack_p.push(i)
        else:
            result += i
    for i in range(0, stack_p.size()):
        y = stack_p.pop()
        result += y
    print ("Postfix of %s" %exp +" is %s" %result)
    
infixToPostfix("A+B*C-D/E") #ABC*+DE/-
