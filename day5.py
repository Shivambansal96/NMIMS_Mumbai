# class Node:

#     def __init__(self, data):
#         self.data = data
#         # newNode.data = 4
#         # secondNode.data = 10
#         self.next = None
#         # newNode.next = None
#         # secondNode.next = None


# class LL:

#     def __init__(self):
#         self.head = None

#     def printList(self):
#         currentNode = newNode

#         while(currentNode is not None):
#             print(currentNode.data, end=" -> ")
#             currentNode= currentNode.next

#         print(None)
        
# newNode = Node(4)
# secondNode = Node(10)
# thirdNode = Node(10)

# newNode.next = secondNode
# secondNode.next = thirdNode

# list1 = LL()
# list1.printList()




# # # # # # Singly Linked List
# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LL:

#     def __init__(self):
#         self.head = None

#     def prepend(self, data):
#         newNode = Node(data)

#         # if self.head is None:
#         #     self.head = newNode
        
#         # else:
#         #     newNode.next = self.head
#         #     self.head = newNode

#         if self.head is not None:
#             newNode.next = self.head

#         self.head = newNode

#     def append(self, data):
#         newNode = Node(data)

#         if self.head is None:
#             self.head = newNode

#         else:
#             currentNode = self.head

#             while currentNode.next is not None:
#                 currentNode = currentNode.next

#             currentNode.next = newNode

#     def deleteStart(self):
        
#         if self.head is None:
#             print("Linked List is Empty!!!")

#         else:
#             self.head = self.head.next

#     def deleteEnd(self):

#         if self.head is None:
#             self.print("LL is Empty !!!")
        
#         else:
#             currentNode = self.head

#             while(currentNode.next.next is not None):
#                 currentNode = currentNode.next

#             currentNode.next = None

#     def printList(self):
#         currentNode = self.head

#         while(currentNode is not None):
#             print(currentNode.data, end=" -> ")
#             currentNode = currentNode.next

#         print(None)

# list1 = LL()
# list1.prepend(2)
# list1.prepend(42)
# list1.append(1)
# list1.prepend(123)
# list1.append(251)
# list1.append(71)
# list1.printList()

# list1.deleteStart()
# list1.printList()
# list1.deleteEnd()

# list1.printList()



# # # # # Doubly Linked List
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LL:

    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode
            self.tail = newNode

        else:
            

    def append(self, data):
        newNode = Node(data)

        if self.head is None:
            self.head = newNode

        else:
            currentNode = self.head

            while currentNode.next is not None:
                currentNode = currentNode.next

            currentNode.next = newNode

    def deleteStart(self):
        
        if self.head is None:
            print("Linked List is Empty!!!")

        else:
            self.head = self.head.next

    def deleteEnd(self):

        if self.head is None:
            self.print("LL is Empty !!!")
        
        else:
            currentNode = self.head

            while(currentNode.next.next is not None):
                currentNode = currentNode.next

            currentNode.next = None

    def printList(self):
        currentNode = self.head

        while(currentNode is not None):
            print(currentNode.data, end=" -> ")
            currentNode = currentNode.next

        print(None)

list1 = LL()
list1.prepend(2)
list1.printList()