class DataNode:
    def __init__(self, input_name):
        self.name = input_name
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.count = 0
        self.head = None

    def traverse(self):
        start = self.head
        if self.head == None:
            print("This is an empty list.")
        else:
            start = self.head
            while start != None:
                print("-->", start.name, end= " ")
                start = start.next
            print("")

    def insertFront(self, data):
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
        else:
            pNew.next = self.head
            self.head = pNew
            self.count += 1

    def insertLast(self, data):
        pNew = DataNode(data)
        if self.head == None:
            self.head = pNew
        else:
            start = self.head
            while start.next != None:
                start = start.next
            start.next = pNew
        self.count += 1
            
    def insertBefore(self, node, data):
        pNew = DataNode(data)
        prev = None
        start = self.head
        if self.head.name == node:
            pNew.next = self.head
            self.head = pNew
            return
        while (start != None) and (start.name != node):
            
            if start.next == None:
                print("Cannot insert, %s does not exist." %node)
                return
            prev = start
            start = start.next
        else:
            prev.next = pNew
            pNew.next = start
            
    def delete(self, data):
        start = self.head
        prev = self.head
        if start.name == data:
            self.head = self.head.next
            return
        while start.name != data:
            if start.next == None:
                print("Cannot delete, %s does not exist." %data)
                return
            prev = start
            start = start.next
        prev.next = start.next

mylist = SinglyLinkedList()
mylist.insertFront("Max")
mylist.insertLast("Kan")
mylist.insertFront("Bill")
mylist.insertLast("Big")
mylist.insertBefore("Max", "Alex")
mylist.traverse()
mylist.delete("Bill")
mylist.traverse()




