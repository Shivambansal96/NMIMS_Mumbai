# # class Stk:

# #     def __init__(self):
# #         self.stk = []
# #         print("Created a Stack !!!")

# #     def push(self, data):
# #         self.stk.append(data)

# #     def peek(self):
# #         return self.stk[-1]
    
# #     def isEmpty(self):
# #         return len(self.stk) == 0
    
# #     def pop(self):
# #         if self.isEmpty():
# #             print("Stack is Empty!!!")
        
# #         else:
# #             top = self.stk[-1]
# #             self.stk.pop(-1)
# #             # arr.pop(-1)
# #             return top
        
# #     def printStk(self):
# #         while(not(self.isEmpty())):
# #             print(f" | {self.pop()} | ")
# #             print(" |----|")

# #         print()

# # def validParentheses(s):
# #     for i in s:
# #         if(i in "({["):
# #             stk.push(i)

# #         else:
# #             if((i == ")" and stk.peek() == "(") or (i == "}" and stk.peek() == "{") or (i == "]" and stk.peek() == "[")):
# #                 stk.pop()

# #             else:
# #                 return False

# #     return True

        

        
# # stk = Stk()
# # # stk.push(12)
# # # stk.push(24)
# # # stk.push(39)

# # # stk.pop()

# # # stk.push(45)
# # # stk.push(69)

# # # stk.printStk()


# # # s = "[(){}]()"
# # s = "(((())))"
# # print(validParentheses(s))



# # class Queue:

# #     def __init__(self):
# #         self.q = []

# #     def isEmpty(self):
# #         return len(self.q) == 0
    
# #     def peek(self):
# #         return self.q[0]          # First Element
    
# #     def push(self, data):
# #         self.q.append(data)

# #     def pop(self):
# #         if self.isEmpty():
# #             print("Queue is Empty")

# #         else:
# #             top = self.peek()
# #             self.q.pop(0)             # self.q.pop(top)
# #             return top
        
# #     def printQueue(self):

# #         for i in self.q:
# #             print(f"{i} ", end=" | ")

# # q = Queue()
# # q.push(88)
# # q.push(12)
# # q.push(1)
# # q.push(43)

# # q.pop()

# # q.peek()
# # q.printQueue()



# class DeQueue:

#     def __init__(self):
#         self.dq = []

#     def isEmpty(self):
#         return len(self.dq) == 0
    
#     def peek(self):
#         return self.dq[0]          # First Element
    
#     def push(self, data):
#         self.dq.append(data)

#     def pushLeft(self, data):
#         self.dq.insert(0, data)

#     def pop(self):
#         if self.isEmpty():
#             print("DeQueue is Empty")

#         else:
#             top = self.peek()
#             self.dq.pop(-1)             # self.q.remove(top)
#             return top
        
#     def popLeft(self):
#         if self.isEmpty():
#             print("DeQueue is Empty")

#         else:
#             last = self.dq[0]
#             self.dq.pop(0)             # self.q.remove(last)
#             return last
        
#     def printDeQueue(self):

#         for i in self.dq:
#             print(f"{i} ", end=" | ")

# dq = DeQueue()
# dq.push(88)
# dq.push(12)
# dq.push(1)
# dq.push(43)

# dq.popLeft()

# print(dq.peek())
# dq.printDeQueue()



# # from collections import deque
# # dq = deque()

# # # dq.append(10)
# # # dq.append(20)
# # print(dq)
# # arr = {10, 20}
# # dq.extend(arr)
# # print(dq)
# # dq.appendleft(5)
# # print(dq)
# # dq.pop()
# # print(dq)



# # # # Linear Search
# arr = [32, 42, 78, 99, 100, 109]

# target = int(input("Enter num: "))

# for i in range(len(arr)):
#     if (arr[i] == target):
#         print(f"Target value {arr[i]} is at index {i}")
#         break
# else:
#     print("Target is NOT present in the list")



# # # # # Binary Search

# def binarySearch(arr, target):

#     start = 0
#     end = len(arr) - 1

#     while(start <= end):

#         mid = (start + end) // 2

#         if(arr[mid] == target):
#             return mid

#         elif(arr[mid] > target):
#             end = mid - 1

#         else:
#             start = mid + 1

#     # return "Not Found"
#     return -1

# arr = [32, 42, 78, 99, 100, 109]
# target = int(input("Enter Num: "))
# res = binarySearch(arr, target)

# if(res > 0):
#     print(f"Target value {target} is at index {res}")
# else:
#     print("Target NOT Found !!!")




