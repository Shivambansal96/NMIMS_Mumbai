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
        self.postOrder(root.right)
        print(root.data, end=" ")

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

        return current
    

    def delete(self, root, val):

        if root is None:
            return None
        
        if (val < root.data):
            root.left = self.delete(root.left, val)

        elif(val > root.data):
            root.right = self.delete(root.right, val)

        else:  # Node Found

            # 0 Child
            if root.left is None and root.right is None: 
                return None
            
            # 1 Child

            if root.left is None:
                return root.right
            
            if root.right is None:
                return root.left

            # 2 child
            iso = self.smallestValue(root.right)
            root.data = iso.data
            self.delete(root.right, iso.data)


        return root

bst = BST()

root = None
arr = [20, 10, 30, 5, 15, 25, 40, 2, 8, 12, 18, 22, 28, 35, 50, 32, 38]
for i in arr:
    root = bst.insert(root, i)


bst.inOrder(root)
print()
# root = bst.delete(root, 8)
root = bst.delete(root, 30)
bst.inOrder(root)
print()



# bst.preOrder(root)
# print()
# bst.inOrder(root)
# print()
# bst.postOrder(root)



# root = bst.insert(20)
# root = bst.insert(10)
# root = bst.insert(30)
# root = bst.insert(5)
# root = bst.insert(15)
# root = bst.insert(25)
# root = bst.insert(40)
# root = bst.insert(2)
# root = bst.insert(8)
# root = bst.insert(12)
# root = bst.insert(18)
# root = bst.insert(22)
# root = bst.insert(28)
# root = bst.insert(35)
# root = bst.insert(50)
# root = bst.insert(32)
# root = bst.insert(38)

    

    
    
