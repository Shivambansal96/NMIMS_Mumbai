# # # # def addition(a, b):
# # # #     sum = a + b
# # # #     print(sum)
# # # #     return 25

# # # # addition(4, 5)


# # # def show(n):
# # #     if(n == 0):        # BASE CASE
# # #         return

# # #     print("BEFORE INSIDE THE FUNCTION", n)
# # #     show(n - 1)        # Recursive Case
# # #     print("AFTER INSIDE THE FUNCTION", n)

# # # n = 3
# # # print("BEFORE OUTSIDE THE FUNCTION", n)
# # # show(n)
# # # print("AFTER OUTSIDE THE FUNCTION", n)



# # # def printNum(n):
# # #     if (n == 0):
# # #         return 
    
# # #     print(n)
# # #     printNum(n - 1)

# # # printNum(10)


# # # def printNum(i, n):
# # #     if (i == n):
# # #         return
    
# # #     print(i)
# # #     printNum(i + 1, n)

# # # n = int(input("Enter a num: "))
# # # printNum(1, n+1)


# # # def naturalSum(n):
# # #     if (n == 0):
# # #         return 0
    
# # #     return n + naturalSum(n - 1)

# # # res = naturalSum(5)
# # # print(res)



# # # def factorial(n):
# # #     if (n == 0 or n == 1):
# # #         return 1
    
# # #     return n * factorial(n - 1)

# # # res = factorial(10)
# # # print(res)






# # def factorial(n):
# #     if (n == 0 or n == 1):
# #         return 1
    
# #     return n * factorial(n - 1)

# # n = 5
# # r = 3
# # num =  factorial(n)
# # denom = factorial(n - r)
# # permutation = num / denom

# # print(f"Permutation = {permutation}")

# # combination = factorial(n) / (factorial(r) * factorial(n - r))
# # print(f"Combination = {combination}")


# ##### 0 1 1 2 3 5 8 13 21 34 55

# def fibonacci(n):
#     if n == 0:
#         return 0

#     if n == 1:
#         return 1
    
#     return fibonacci(n -1) + fibonacci(n - 2)

# print("Fibonacci Series = ", end="")
# for i in range(3):
#     print(fibonacci(i), end=" ")



# # ## # # BackTracking
# def countPaths(i, j, n, m):
#     # Dead End
#     if (i == n or j == m):
#         return 0

#     # Reach Destination
#     if(i == n - 1 and j == m - 1):
#         return 1

#     # Right Path
#     rightPath = countPaths(i, j + 1, n, m)

#     # Down Path
#     downPath = countPaths(i + 1, j, n, m)

#     return downPath + rightPath

# n = m = 3
# print(countPaths(0, 0, n, m))



class Node:
    def __init__(self, data):
        self.data = data
        # newNode.data = 45
        self.next = None
        # newNode.next = None

class LL:

    def printList(self):
        currentNode = firstNode

        while(currentNode != None):
            print(currentNode.data, end="->")

            currentNode = currentNode.next

        print(None)
        

        
firstNode = Node(4)
firstNode.next = Node(10)
firstNode.next.next= Node(100)

list1 = LL()
list1.printList()
