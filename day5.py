# # class Node:

# #     def __init__(self, data):
# #         self.data = data
# #         # newNode.data = 4
# #         # secondNode.data = 10
# #         self.next = None
# #         # newNode.next = None
# #         # secondNode.next = None


# # class LL:

# #     def __init__(self):
# #         self.head = None

# #     def printList(self):
# #         currentNode = newNode

# #         while(currentNode is not None):
# #             print(currentNode.data, end=" -> ")
# #             currentNode= currentNode.next

# #         print(None)
        
# # newNode = Node(4)
# # secondNode = Node(10)
# # thirdNode = Node(10)

# # newNode.next = secondNode
# # secondNode.next = thirdNode

# # list1 = LL()
# # list1.printList()




# # # # # # # Singly Linked List
# # class Node:

# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None

# # class LL:

# #     def __init__(self):
# #         self.head = None

# #     def prepend(self, data):
# #         newNode = Node(data)

# #         # if self.head is None:
# #         #     self.head = newNode
        
# #         # else:
# #         #     newNode.next = self.head
# #         #     self.head = newNode

# #         if self.head is not None:
# #             newNode.next = self.head

# #         self.head = newNode

# #     def append(self, data):
# #         newNode = Node(data)

# #         if self.head is None:
# #             self.head = newNode

# #         else:
# #             currentNode = self.head

# #             while currentNode.next is not None:
# #                 currentNode = currentNode.next

# #             currentNode.next = newNode

# #     def deleteStart(self):
        
# #         if self.head is None:
# #             print("Linked List is Empty!!!")

# #         else:
# #             self.head = self.head.next

# #     def deleteEnd(self):

# #         if self.head is None:
# #             self.print("LL is Empty !!!")

# #         elif self.head.next is None:
# #             self.head = None
        
# #         else:
# #             currentNode = self.head

# #             while(currentNode.next.next is not None):
# #                 currentNode = currentNode.next

# #             currentNode.next = None

# #     def printList(self):
# #         currentNode = self.head

# #         while(currentNode is not None):
# #             print(currentNode.data, end=" -> ")
# #             currentNode = currentNode.next

# #         print(None)

# # list1 = LL()
# # # list1.prepend(2)
# # # list1.prepend(42)
# # # list1.append(1)
# # # list1.prepend(123)
# # # list1.append(251)
# # # list1.append(71)
# # # list1.printList()

# # list1.append(98)
# # # list1.append(42471)
# # # list1.append(7421)
# # # list1.append(7134)
# # list1.printList()
# # # list1.deleteStart()
# # list1.deleteEnd()
# # list1.printList()



# # # # # # # Doubly Linked List
# # class Node:

# #     def __init__(self, data):
# #         self.data = data
# #         self.next = None
# #         self.prev = None

# # class LL:

# #     def __init__(self):
# #         self.head = None
# #         self.tail = None

# #     def prepend(self, data):
# #         newNode = Node(data)

# #         if self.head is None:
# #             self.head = newNode
# #             self.tail = newNode

# #         else:

# #             newNode.next = self.head
# #             self.head.prev = newNode

# #             self.head = newNode
            

# #     def append(self, data):
# #         newNode = Node(data)

# #         if self.head is None:
# #             self.head = newNode
# #             self.tail = newNode

# #         else:
# #             self.tail.next = newNode
# #             newNode.prev = self.tail
# #             self.tail = newNode

# #     def deleteStart(self):
        
# #         if self.head is None:
# #             print("Linked List is Empty!!!")

# #         # elif (self.head == self.tail):
# #         elif (self.head.next is None):
# #             self.head = None
# #             self.tail = None

# #         else:
# #             self.head = self.head.next
# #             self.head.prev = None
            

# #     def deleteEnd(self):

# #         if self.head is None:
# #             self.print("LL is Empty !!!")

# #         elif (self.head == self.tail):
# #             self.head = None
# #             self.tail = None
        
# #         else:
# #             self.tail = self.tail.prev
# #             self.tail.next = None



# #     def printList(self):
# #         currentNode = self.head

# #         while(currentNode is not None):
# #             print(currentNode.data, end=" <-> ")
# #             currentNode = currentNode.next

# #         print(None)

# # list1 = LL()
# # list1.prepend(2)
# # list1.prepend(13)
# # list1.append(23)

# # list1.printList()
# # list1.deleteStart()
# # list1.append(123)
# # list1.prepend(99)
# # list1.printList()





# # # # # # Circular Linked List
# class Node:

#     def __init__(self, data):
#         self.data = data
#         self.next = None
#         self.prev = None

# class LL:

#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def prepend(self, data):
#         newNode = Node(data)

#         if self.head is None:
#             self.head = newNode
#             self.tail = newNode
#             # newNode.prev = self.tail   # NEVER USE THIS (INFINITE LOOP)
#             # newNode.next = self.head   # NEVER USE THIS (INFINITE LOOP)

#         # elif self.head.next is None:
#         #     newNode.next = self.head
#         #     newNode.prev = self.head
#         #     self.head.prev = newNode
#         #     self.head.next = newNode
#         #     self.head = newNode

#         else:
#             newNode.next = self.head
#             newNode.prev = self.tail
#             self.head.prev = newNode
#             self.tail.next = newNode
#             self.head = newNode

#     def append(self, data):
#         newNode = Node(data)

#         if self.head is None:
#             self.head = newNode
#             self.tail = newNode

#         else:
#             newNode.next = self.head
#             newNode.prev = self.tail
#             self.head.prev = newNode
#             self.tail.next = newNode
#             self.tail = newNode

#     def deleteStart(self):
        
#         if self.head is None:
#             print("Linked List is Empty!!!")

#         # elif (self.head == self.tail):
#         elif (self.head.next is None):
#             self.head = None
#             self.tail = None

#         else:
#             self.head = self.head.next
#             self.head.prev = self.tail
#             self.tail.next = self.head
            

#     def deleteEnd(self):

#         if self.head is None:
#             print("LL is Empty !!!")

#         elif (self.head == self.tail):
#             self.head = None
#             self.tail = None

#         else:
#             self.tail = self.tail.prev
#             self.tail.next = self.head
#             self.head.prev = self.tail

#     def printList(self):
#         currentNode = self.head

#         while(currentNode is not self.tail):
#             print(currentNode.data, end=" <-> ")
#             currentNode = currentNode.next

#         if(self.head is not None):
#             print(currentNode.data, end=" <-> ")
#             # print(self.tail.data, end=" <-> ")

#         print(None)

# list1 = LL()
# list1.prepend(242)
# list1.append(111)
# list1.printList()
# list1.prepend(2)
# list1.append(99)
# list1.printList()
# list1.deleteEnd()
# list1.deleteStart()
# list1.printList()





# ## # # Stack

class Stk:

    def __init__(self):
        self.stk = []

    def push(self, data):
        self.stk.append(data)

    def peek(self):
        # return self.stk[len(self.stk) - 1]
        return self.stk[-1]

    def isEmpty(self):
        return len(self.stk) == 0
    
    def pop(self):

        if self.isEmpty():
            print("Stack is Empty !!!")
            return

        topElement = self.stk[-1]
        return self.stk.remove(topElement)
    

    def printStack(self):
        for i in self.stk:
            print(f" | {i}  |")
            print(" | --- |")

        print()

stack1 = Stk()
# stack1.push(45)
# stack1.push(12)
# stack1.printStack()

stack1.pop()
stack1.printStack()


