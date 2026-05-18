# # # # # # # # arr = []
# # # # # # # # for i in range(1, 11):
# # # # # # # #     arr.append(i*i)

# # # # # # # # print(f"Array = {arr}")


# # # # # # # # # a = (5, 7, 9, 8, 7)

# # # # # # # # # # print(type(a))
# # # # # # # # # print(a.index(7))
# # # # # # # # # print(a.count(7))


# # # # # # # # arr = [1, 2, 3]

# # # # # # # # arr2 = arr

# # # # # # # # arr2.append(5)
# # # # # # # # arr.append(90)

# # # # # # # # print(arr)
# # # # # # # # print(arr2)


# # # # # # # # t = ("Z", "A", "R", "C")
# # # # # # # # print(sorted(t))

# # # # # # # # # arr = list(t)

# # # # # # # # # # list.sort(arr)
# # # # # # # # # arr.sort()
# # # # # # # # # print(arr)


# # # # # # # tup = (32, 56, 775, 12, 11, 90, 97)

# # # # # # # countEven = 0
# # # # # # # countOdd = 0
# # # # # # # evenList = []
# # # # # # # oddList = []

# # # # # # # for i in tup:
# # # # # # #     if(i % 2 == 0):
# # # # # # #         countEven += 1
# # # # # # #         evenList.append(i)

# # # # # # #     else:
# # # # # # #         countOdd += 1
# # # # # # #         oddList.append(i)

# # # # # # # print(f"Total Even Numbers = {countEven} which are {evenList}")
# # # # # # # print(f"Total Odd Numbers = {countOdd} which are {oddList}")



# # # # # # # setA = {1, 2, 2, 2, 3}
# # # # # # # setB = set()

# # # # # # # setC = {53, 13, 567, 32, 78, 7, 90}
# # # # # # # setC.pop()


# # # # # # # setA.pop()
# # # # # # # print(setC)

# # # # # # # print(type(setB))


# # # # # # # setA = {1, 2, 3}
# # # # # # # setB= {3, 4, 5}

# # # # # # # print(setA.union(setB))
# # # # # # # print(setA.intersection(setB))


# # # # # # classRooms = {"C", "Java", "js", "Python", "C", "Python", "js"}

# # # # # # print(len(classRooms))


# # # # # # arr = [3, 5, 7, 3, 9, 5, 3, 9]
# # # # # # dupSet = set()

# # # # # # for i in range(len(arr)):
# # # # # #     for j in range(i+1, len(arr)):
# # # # # #         if(arr[i] == arr[j]):
# # # # # #             dupSet.add(arr[i])
# # # # # #             break

# # # # # # print(dupSet)
        




# # # # # # arr = [3, 5, 7, 3, 9, 5, 3, 9]
# # # # # # dupArr = []

# # # # # # for i in range(len(arr)):
# # # # # #     for j in range(i+1, len(arr)):
# # # # # #         if(arr[i] == arr[j]):

# # # # # #             if arr[i] not in dupArr:
# # # # # #                 dupArr.append(arr[i])
# # # # # #                 break
                
# # # # # #             else:
# # # # # #                 break

# # # # # # print(dupArr)
        


# # # # # # arr = [3, 5, 7, 3, 9, 5, 3, 9]
# # # # # # dupSet = []
# # # # # # visited = set()

# # # # # # for i in range(len(arr)):
# # # # # #     if arr[i] not in visited:
# # # # # #         visited.add(arr[i])
# # # # # #     else:
# # # # # #         dupSet.append(arr[i])

# # # # # # print(dupSet)


# # # # # myDict = {
# # # # #     'name': "Shivam",
# # # # #     'isTrainer': True,
# # # # #     'price': 99,
# # # # #     'marks': {
# # # # #         'Java': 95,
# # # # #         'Python': 92,
# # # # #         'webDev': 99
# # # # #     }
# # # # # }

# # # # # # print(myDict['marks']['webDev'])
# # # # # # print(myDict.keys())
# # # # # # print(myDict['marks'].keys())
# # # # # # print(myDict.values())
# # # # # # print(myDict['marks'].values())

# # # # # # print(myDict.items())

# # # # # # print(myDict.get('names'))
# # # # # # # print(myDict['names'])
# # # # # # print("Code Ends")

# # # # # myDict.update({
# # # # #     'name': "Mohini",
# # # # #     'clgName': "NMIMS"
# # # # # })

# # # # # print(myDict)


# # # # myDict = {}


# # # # for i in range(3):
# # # #     myDict.update({
# # # #         input("Enter subject name: ") : input("Enter marks: ")
# # # #     })

# # # # print(myDict)



# # # myDict = {}
# # # for i in range(1, 11):
# # #     myDict.update({i:i**2})

# # # print(myDict)




# # # def addition(a, b):
# # #     sum = a + b
# # #     print(sum)
# # #     return "UNDERSTOOD NOW !!!"

# # # print(addition(4, 5))








# # # myDict = {
# # #     3: 3,
# # #     5: 2,
# # #     7: 1,
# # #     9: 2
# # # }


# # # arr = [3, 5, 7, 3, 9, 5, 3, 9]
# # # myDict = {}
# # # for i in arr:
# # #     if i not in myDict:
# # #         myDict.update({i: 1})

# # #     else:
# # #         myDict.update({i: myDict.get(i) + 1})

# # # print(myDict)



# # # -------------------------------------------- #



# # # class Student:
# # #     trainerName = "Shivam Bansal"
# # #     name = "Shreyas"

# # #     def __init__(self):
# # #         # print(f"INSIDE = {self}")
# # #         pass

# # # s1 = Student()
# # # # print(s1.trainerName)
# # # # print(Student.trainerName)
# # # # print(f'OUTSIDE s1 = {s1}')
# # # print(s1.name)

# # # print("_----------------_")

# # # s2 = Student()
# # # # print(f'OUTSIDE s2 = {s2}')
# # # print(s2.name)



# # # class Student:

# # #     # def __init__(s1, name):
# # #     def __init__(self, name):
# # #         self.fullName = name
# # #         # s1.fullName = "Shivam"
# # #         # s2.fullName = "Mohini"

# # # s1 = Student("Shivam")
# # # print(s1.fullName)

# # # s2 = Student("Mohini")
# # # print(s2.fullName)



# # # # ## # # Non-parameterized Constructor
# # # class Student:

# # #     # def __init__(self):
# # #     #     pass

# # #     def hello(self):
# # #         print(f"HELLO")

# # # s1 = Student()
# # # s1.hello()


# # # # ## # # Parameterized Constructor
# # # class Student:

# # #     def __init__(self, name):
# # #         self.name = name

# # # s1 = Student("Shivam")
# # # print(s1.name)




# # # # ## # # Parameterized Constructor
# # # class Student:

# # #     def __init__(self, name="anonymous"):
# # #         self.name = name

# # # s1 = Student("Shivam")
# # # print(s1.name)

# # # s2 = Student()
# # # print(s2.name)


# # # class Student:

# # #     name = "Shivam"
# # #     isTrainer = True
# # #     currentClg = "NMIMS"

# # # s1 = Student()
# # # # del s1.name
# # # del s1
# # # print(s1.name)


# # # s2 = Student()
# # # print(s2.name)


# # # *args
# # class Student:
# #     def __init__(self, name, m1, m2, m3):
# #         self.name = name
# #         self.m1 = m1
# #         self.m2 = m2
# #         self.m3 = m3

# #     def getAvg(self):
# #         avg = (self.m1 + self.m2 + self.m3) / 3
# #         print(f"Average of {self.name} = {avg:.2f}")
# #         return avg

# # s1 = Student("Shivam", 91, 77, 11)
# # # print(s1.getAvg())
# # # s1.getAvg()


# # s2 = Student("Mohini", 9, 10, 788)
# # # s2.getAvg()

# # topMarks = max(s1.getAvg(), s2.getAvg())    
# # print(topMarks)






# class Circle:

#     def __init__(self, radius):
#         self.r = radius
    
#     def getArea(self):
#         area = (22/7) * self.r **2
#         print(f"Area = {area:.2f}")

#     def getPerimeter(self):
#         perimeter = (22/7) * self.r **2
#         print(f"Perimeter = {perimeter:.2f}")

# c1 = Circle(4)
# c1.getArea()



class Student:

    @staticmethod
    def welcome():
        print("Welcome Student")

s1 = Student()
s1.welcome()
