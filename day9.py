# # # # import heapq as heap

# # # # pq = []

# # # # heap.heappush(pq, 2)
# # # # heap.heappush(pq, 5)
# # # # heap.heappush(pq, 6)
# # # # heap.heappush(pq, 7)
# # # # heap.heappush(pq, 95)
# # # # heap.heappush(pq, 50)

# # # # print(pq)
# # # # heap.heappush(pq, 1)
# # # # print(pq)
# # # # heap.heappop(pq)
# # # # print(pq)




# # # import heapq as heap

# # # pq = []

# # # heap.heappush(pq, 2)
# # # heap.heappush(pq, 5)
# # # heap.heappush(pq, 6)
# # # heap.heappush(pq, 7)
# # # # heap.heappush(pq, 95)
# # # # heap.heappush(pq, 50)

# # # print(pq)
# # # heap.heappush(pq, 4)
# # # print(pq)
# # # heap.heappop(pq)
# # # print(pq)



# # import heapq as heap

# # pq = [32, 56, 2, 77, 90, 13]

# # print(pq)

# # heap.heapify(pq)

# # print(pq)


# # # # # # Frequency Counter

# arr = [2, 2, 3, 4, 4, 5, 6, 6]

# freqCounter = {}

# # for i in arr:
# #     if i in freqCounter:
# #         # freqCounter.update({i : freqCounter.get(i) + 1})
# #         freqCounter.update({i : freqCounter[i] + 1})

# #     else:
# #         freqCounter.update({i : 1})

# # print(freqCounter)



# # # # # # Method 2
# # arr = [2, 2, 3, 4, 4, 5, 6, 6]

# # freqCounter = {}

# # for i in arr:
# #     if i in freqCounter:
# #         freqCounter[i] +=1

# #     else:
# #         freqCounter[i] = 1

# # print(freqCounter)


# # # # # # Method 3
# # from collections import Counter

# # arr = [2, 2, 3, 4, 4, 5, 6, 6]
# # freqCount = Counter(arr)

# # # print(freqCount)

# # for key, val in freqCount.items():
# #     print(f"{key}, {val}")



# # # # ## # Top Frequent k Elements
# # from collections import Counter
# # import heapq

# # arr = [1, 1, 1, 2, 2, 3, 4, 4, 4, 5]
# # k = 2

# # heap = []
# # freq = Counter(arr) # {1:3, 2:2, 3:1, 4:3, 5:1}

# # for key, count in freq.items():
# #     heapq.heappush(heap, (-count, key))

# # res = []
# # for i in range(k):
# #     count, key = heapq.heappop(heap)
# #     res.append(key)

# # print(res)



# # # # # K Smallest Elements

# import heapq

# arr = [21, 314, 65, 2, 78, 9, 99]
# k = 2

# heapq.heapify(arr)

# res = []

# for i in range(k):
#     res.append(heapq.heappop(arr))

# print(res)












# # # ## # ## Fibonacci Recursive only Method
# class Solution:
#     def fib(self, n: int) -> int:

#         if n == 0:
#             return 0
        
#         if n == 1:
#             return 1
        
#         return self.fib(n - 1) + self.fib(n - 2)
    

# s1 = Solution()
# res = s1.fib(6)
# print(res)


# # # ## # ## Fibonacci DP(Memoization Method)
# class Solution:
#     def fib(self, n: int) -> int:

#         freq = {
#             0 : 0,
#             1 : 1
#         }

#         def fibonacci(c):
#             if c in freq:
#                 return freq[c]

#             else:
#                 freq[c] = fibonacci(c - 1) + fibonacci(c - 2)
#                 return freq[c]

#         return fibonacci(n)

# s1 = Solution()
# res = s1.fib(7)
# print(res)



# # # # # # # # # Fibonacci DP(Tabulation) Method 3

# n = 6    # 8

# arr = [0] * (n+1)
# arr[0] = 0
# arr[1] = 1

# print(arr)

# for i in range(2, len(arr)):
#     arr[i] = arr[i - 1] + arr[i - 2]

# print(arr)
# print(arr[n])




# # # # # # # # Fibonacci DP(Space Optimization) Method 4

n = 6    # 8
prev = 0
current = 1

for i in range(2, n+1):
    temp = prev + current
    prev = current
    current = temp

print(current)