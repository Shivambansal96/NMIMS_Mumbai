# # # # # for i in range(1, 6):
# # # # #     if(i == 3):
# # # # #         break
    
# # # # #     print(i)
# # # # # else:
# # # # #     print("Code Ends")

# # # # # # # # # Palindrome (CONverging Pointers) Method 1
# # # # # s = input("Enter a word: ")
# # # # # start = 0
# # # # # end = len(s) - 1
# # # # # while(start <= end):

# # # # #     if(s[start] != s[end]):
# # # # #         print("Not Palindrome")
# # # # #         break

# # # # #     if(start == len(s) // 2):
# # # # #         print("Palindrome")
# # # # #     else:
# # # # #         pass

# # # # #     start += 1
# # # # #     end -= 1


# # # # # # # # Palindrome (CONverging Pointers) Method 2
# # # # s = input("Enter a word: ")
# # # # start = 0
# # # # end = len(s) - 1

# # # # palindrome = False
# # # # while(start <= end):

# # # #     if(s[start] != s[end]):
# # # #         palindrome = False
# # # #         break
# # # #     else:
# # # #         palindrome = True

# # # #     start += 1
# # # #     end -= 1

# # # # print(palindrome)


# # # # # # Merge 2 Sorted Arrays using Parallel Pointers
# # # a = [2, 5, 9, 12, 98]
# # # b = [4, 8 , 16]
# # # sortedArr = []

# # # i = 0
# # # j = 0

# # # while(i < len(a) and j < len(b)):
# # #     if(a[i] < b[j]):
# # #         sortedArr.append(a[i])
# # #         i += 1
# # #     else:
# # #         sortedArr.append(b[j])
# # #         j += 1

# # # while(i < len(a)):
# # #     sortedArr.append(a[i])
# # #     i+=1 

# # # while(j < len(b)):
# # #     sortedArr.append(b[j])
# # #     j += 1

# # # print(sortedArr)

    



# # # # # # # Remove Duplicates using Trigger-based pointer(fast-slow pointers)
# # # arr = [1, 2, 2, 3, 5, 5, 6]

# # # i = 0
# # # j = 1

# # # while(j < len(arr)):
# # #     if(arr[i] != arr[j]):
# # #         i += 1
# # #         arr[i] = arr[j]

# # #     j += 1

# # # print(arr[:i+1])



# # # # # # Remove Duplicates using Trigger-based pointer(fast-slow pointers)
# # arr = [1, 2, 2, 3, 5, 5, 6, 2]

# # i = 0
# # j = 1

# # while(j < len(arr)):
# #     if arr[j] not in arr[:i + 1]:
# #         i += 1
# #         arr[i] = arr[j]

# #     j += 1

# # print(arr[:i+1])




# # ## # Maximum Average SubArray I
# arr = [1,12,-5,-6,50,3]
# k = 4
# i = 0
# j = k
# maxAvg = 0

# while(j < len(arr)):

#     currentAvg = sum(arr[i:j]) / k
#     maxAvg = max(currentAvg, maxAvg)

#     i+= 1
#     j += 1

# print(maxAvg)

arr = [1, 12, -5, -6, 50, 3]
k = 4

currentSum = 0

for i in range(k):
    currentSum += arr[i]

maxSum = currentSum

for i in range(k , len(arr)):
    currentSum += arr[i]
    currentSum -= arr[i - k]
    maxSum = max(currentSum, maxSum)

maxAvg = maxSum/k
print(f"Max Average = {maxAvg}")



