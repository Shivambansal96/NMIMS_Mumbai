# # class Node:

# #     def __init__(self, data, left=None, right=None):
# #         self.data = data
# #         self.left = left
# #         self.right = right


# # root = Node(5)
# # root.left = Node(10)
# # root.right = Node(12)
# # root.left.left = Node(23)
# # root.left.right = Node(25)
# # root.right.left = Node(16)
# # root.right.right = Node(2)

# # root.left.left.left = Node(23)
# # root.left.left.right = Node(23)

# # root.left.right.left = Node(25)
# # root.left.right.right = Node(25)


# from collections import deque

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BT:

#     # def __init__(self):
#     #     self.root = None
        
#     def insert(self, root, data):
#         newNode = Node(data)

#         if root is None:
#             return newNode
        
#         dq = deque([root])

#         while dq:
#             root = dq.popleft()

#             if root.left is None:
#                 root.left = newNode
#                 return
#             else:
#                 dq.append(root.left)

#             if root.right is None:
#                 root.right = newNode
#                 return
#             else:
#                 dq.append(root.right)

# bt = BT()

# root = None
# bt.insert(root, 4)






# from collections import deque

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class BST:

#     # def __init__(self):
#     #     self.root = None
        
#     def insert(self, root, data):
#         newNode = Node(data)

#         if root is None:
#             return newNode
        
#         dq = deque([root])

#         while dq:
#             root = dq.popleft()

#             if(data < root.data):
#                 if root.left is None:
#                     root.left = newNode
#                     return
#                 else:
#                     dq.append(root.left)

#             else:
#                 if root.right is None:
#                     root.right = newNode
#                     return
#                 else:
#                     dq.append(root.right)

# bst = BST()

# root = None
# bst.insert(root, 4)







class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:

    def insert(self, root, data):
        newNode = Node(data)

        if root is None:
            return newNode
        
        if(data < root.data):
            root.left = self.insert(root.left, data)

        else:
            root.right = self.insert(root.right, data)

        return root



    def preOrder(self, root):

        if root is None:
            return

        print(root.data, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self, root):

        if root is None:
            return

        self.inOrder(root.left)
        print(root.data, end=" ")
        self.inOrder(root.right)


    def postOrder(self, root):

        if root is None:
            return

        self.postOrder(root.left)
        print(root.data, end=" ")
        self.postOrder(root.right)

    def heightOfTree(self, root):

        if root is None:
            return 0
        
        leftHeight = self.heightOfTree(root.left)
        rightHeight = self.heightOfTree(root.right)

        return (max(leftHeight, rightHeight) + 1)

    def countNumberOfNodes(self, root):
        
        if root is None:
            return 0
        
        leftCount = self.countNumberOfNodes(root.left)
        rightCount = self.countNumberOfNodes(root.right)

        return leftCount + rightCount + 1

    def sumOfAllNodes(self, root):
        
        if root is None:
            return
    
        leftSum = self.sumOfAllNodes(root.left)
        rightSum = self.sumOfAllNodes(root.right)

        return leftSum + rightSum + root.data
    
    def binarySearch(self, root, target):
        
        if root is None:
            return "No Value"
        
        if(target == root.data):
            return "Value Found"

        elif(target < root.data):
            self.binarySearch(root.left, target)

        else:
            self.binarySearch(root.right, target)


    def smallestValue(self, root):

        current = root

        while current.left is not None:
            current = current.left

        return current.data
    
    
