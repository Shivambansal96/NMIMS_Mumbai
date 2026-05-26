# class Node:
#     def __init__(self, data, left=None, right=None):
#         self.data = data
#         self.left = left
#         self.right = right

#     def __str__(self):
#         return str(self.data)

# class BT:

#     def __init__(self):
#         self.root = None

#     def createNode(self, data):
#         newNode = Node(data)

# def preOrder(node):
#     if not node:
#         return 
    
#     preOrder(node.left)
#     preOrder(node.right)
#     print(node)

    



# # bt1 = BT()
# A = Node(1)
# B = Node(2)
# C = Node(3)
# D = Node(4)
# E = Node(5)
# F = Node(6)
# G = Node(7)

# A.left = B
# A.right = C
# B.left = D
# B.right = E
# C.left = F
# C.right = G

# preOrder(A)


from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BT:

    def __init__(self):
        self.root = None

    def createNode(self, data):
        return Node(data)

    def insert(self, root, data):
        newNode = Node(data)

        if root is None:
            self.root = newNode
            return
        
        q = deque([self.root])

        while q:
            root = q.popleft()

            if root.left is None:
                root.left = newNode
                return
            else:
                q.append(root.left)

            if root.right is None:
                root.right = newNode
                return
            else:
                q.append(root.right)

    def preOrder(self, root):
        if root is None:
            return 
        
        print(root.data, end=" -> ")
        self.preOrder(root.left)
        self.preOrder(root.right)


bt = BT()

bt.root = bt.createNode(5)

bt.insert(bt.root, 7)
bt.insert(bt.root, 9)

bt.preOrder(bt.root)
print(None)