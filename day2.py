# # # # # # # # # Single Level Inheritance
# # # # # # class Shape:
# # # # # #     color = "red"

# # # # # # class Triangle(Shape):
# # # # # #     sides = 3

# # # # # # t1 = Triangle()
# # # # # # print(t1.color)


# # # # # # # # # # Multi-Level Inheritance
# # # # # # class Shape:
# # # # # #     color = "red"

# # # # # # class Triangle(Shape):
# # # # # #     sides = 3

# # # # # # t1 = Triangle()
# # # # # # print(t1.color)

# # # # # # class Isosceles(Triangle):
# # # # # #     degree = 180

# # # # # # i1 = Isosceles
# # # # # # print(i1.color)




# # # # # # # # # # Hierarchial Level Inheritance
# # # # # # class Shape:
# # # # # #     color = "red"

# # # # # # class Triangle(Shape):
# # # # # #     sides = 3

# # # # # # t1 = Triangle()
# # # # # # print(t1.color)

# # # # # # class Square(Shape):
# # # # # #     sides = 4

# # # # # # s1 = Square()
# # # # # # print(s1.color)



# # # # # # # # # # Hybrid Level Inheritance
# # # # # # class Shape:
# # # # # #     color = "red"

# # # # # # class Triangle(Shape):
# # # # # #     sides = 3

# # # # # # t1 = Triangle()
# # # # # # print(t1.color)

# # # # # # class Square(Shape):
# # # # # #     sides = 4

# # # # # # s1 = Square()
# # # # # # print(s1.color)

# # # # # # class Isosceles(Triangle):
# # # # # #     degree = 180

# # # # # # i1 = Isosceles
# # # # # # print(i1.color)



# # # # # class Mom:
# # # # #     gender = "Female"

# # # # # class Dad:
# # # # #     gender = "Male"

# # # # # class Me(Dad, Mom):
# # # # #     sex = "M"

# # # # # m1 = Me()
# # # # # print(m1.gender)


# # # # class Employee:

# # # #     def __init__(self, role, dept, salary):
# # # #         self.role = role
# # # #         self.department = dept
# # # #         self.salary = salary

# # # #     def showDetails(self):
# # # #         print(f"Role = {self.role}")
# # # #         print(f"Department = {self.department}")
# # # #         print(f"Salary = {self.salary}")
# # # #         print("----------------------------")

# # # # e1 = Employee("Trainer", "IT", 999)
# # # # # e1.showDetails()

# # # # class Engineer(Employee):

# # # #     def __init__(self, name, age, role, dept, salary):
# # # #         self.name = name
# # # #         self.age = age

# # # #         # Employee().__init__(role, dept, salary)
# # # #         super().__init__(role, dept, salary)

# # # #     def showDetails(self):
# # # #         print(f'Name = {self.name}')
# # # #         print(f'Age = {self.age}')
# # # #         super().showDetails()

# # # #         # return "ABcD"


# # # # eng1 = Engineer("Shivam", 99, "Technical Trainer", "B.Com", 9999)
# # # # print(eng1.showDetails())


# # # class Account:

# # #     def __init__(self, accNum, accPass):
# # #         self.accNum = accNum
# # #         self.__accPass = accPass

# # #     def __showPass(self):
# # #         # print(f"Password = {self.__accPass}")
# # #         return self.__accPass

# # #     def getPass(self):
# # #         return self.__showPass()

# # #     def changePassword(self):
# # #         while True:
# # #             oldPass = input("Enter your old Password: ")
# # #             if(oldPass == self.getPass()):
# # #                 newPass = input("Enter your new Password: ")
# # #                 self.__accPass = newPass
# # #                 break

# # #             else:
# # #                 print("Wrong Password !!!")



# # # a1 = Account(14380100115559, "Shivam@123")
# # # print(a1.accNum)
# # # # print(a1.__accPass)
# # # # a1.__showPass()
# # # a1.changePassword()




# # class Account:

# #     def __init__(self, name, bal):
# #         self.name = name
# #         self.balance = bal

# #     def debit(self):
# #         amount = int(input("Enter the amount you want to debit = "))

# #         if(amount <= self.balance):
# #             self.balance -= amount
# #             print(f"Rs {amount} debited")
# #         else:
# #             print("Insufficient Balance")

# #     def credit(self, amount):
# #         self.balance += amount
# #         print(f"Rs {amount} credited")

# #     def showBalance(self):
# #         print(f"Balance = {self.balance}")

# # a1 = Account("Shivam", 34000)
# # a1.debit()
# # a1.credit(10000)
# # a1.showBalance()


# # # Polymorphism
# class Dog:
#     def sound(self):
#         print("Dog Barks")
# class Cat:
#     def sound(self):
#         print("Cat Meows")
# class Lion:
#     def sound(self):
#         print("Lion roars")

# def sound(Animal):
#     Animal.sound()

# d1 = Dog()
# c1 = Cat()
# l1 = Lion()

# sound(l1)
# sound(d1)
# sound(c1)





# # # Abstraction


from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def walk(self):
        pass
class Dog(Animal):
    def walk(self):
        print("Can walk 4 legs")
class Hen(Animal):
    def walk(self):
        print("Can walk 2 legs")
class Cow(Animal):
    def sound(self):
        print("Cow Moos")

    def walk(self):
        print("Can walk 4 legs with 1 tail")

d1 = Dog()
d1.walk()

h1 = Hen()
h1.walk()

c1 = Cow()
c1.sound()