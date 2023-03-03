class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert(self, data):
        pNew = BSTNode(data)
        prev = None
        start = self.root
        if self.is_empty():
            self.root = pNew
        else:
            while start != None:
                if data < start.data:
                    prev = start
                    start = start.left
                    
                else:
                    prev = start
                    start = start.right
            if prev.data > data:
                prev.left = pNew
            else:
                prev.right = pNew

    def delete(self, data):
        if self.is_empty():
            return None
        
        prev = None
        root = self.root

        while root != None:
            if root.data == data:
                break
            elif root.data > data:
                prev = root
                root = root.left
            else:
                prev = root
                root = root.right
                
        if root == None:
            return None

        if root.left == None and root.right == None:
            if root == self.root:
                self.root = None
            elif prev.left == root:
                prev.left = None
            else:
                prev.right = None

        elif root.left == None:
            if root == self.root:
                self.root = root.right
            elif prev.left == root:
                prev.left = root.right
            else:
                prev.right = root.right

        elif root.right == None:
            if root == self.root:
                self.root = root.left
            elif prev.left == root:
                prev.left = root.left
            else:
                prev.right = root.left

        else:
            parent = root
            check = root.left

            while check.right != None:
                parent = check
                check = check.right

            root.data = check.data

            if parent.left == check:
                parent.left = check.left
            else:
                parent.right = check.left

    def preorder(self, root:BSTNode):
        if root != None:
            print("-->" , root.data, end=' ')
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root:BSTNode):
        if (root != None):
            self.inorder(root.left)
            print("->", root.data, end=' ')
            self.inorder(root.right)

    def postorder(self, root:BSTNode):
        if (root != None):
            self.postorder(root.left)
            self.postorder(root.right)
            print("->", root.data, end=' ')

    def traverse(self):
        print("Preorder", end=' ')
        self.preorder(self.root)
        print()

        print("Inorder", end=' ')
        self.inorder(self.root)
        print()

        print("Postorder", end=' ')
        self.postorder(self.root)
        print()

    def findMin(self):
        if self.is_empty():
            return None
        else:
            pointer = self.root
            while pointer.left != None:
                pointer = pointer.left
        return pointer.data

    def findMax(self):
        if self.is_empty():
            return None
        else:
            pointer = self.root
            while pointer.right != None:
                pointer = pointer.right
        return pointer.data


myBST = BST()
myBST.insert(50); myBST.insert(10)
myBST.insert(100); myBST.insert(1)
myBST.insert(12)
myBST.insert(2)
myBST.insert(3)
myBST.delete(50)
myBST.traverse()

# print("MIN : " , myBST.findMin())
# print("MAX : " , myBST.findMax())
