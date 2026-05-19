# # # # # # Single Level Inheritance
# # # class Shape:
# # #     color = "red"

# # # class Triangle(Shape):
# # #     sides = 3

# # # t1 = Triangle()
# # # print(t1.color)


# # # # # # # Multi-Level Inheritance
# # # class Shape:
# # #     color = "red"

# # # class Triangle(Shape):
# # #     sides = 3

# # # t1 = Triangle()
# # # print(t1.color)

# # # class Isosceles(Triangle):
# # #     degree = 180

# # # i1 = Isosceles
# # # print(i1.color)




# # # # # # # Hierarchial Level Inheritance
# # # class Shape:
# # #     color = "red"

# # # class Triangle(Shape):
# # #     sides = 3

# # # t1 = Triangle()
# # # print(t1.color)

# # # class Square(Shape):
# # #     sides = 4

# # # s1 = Square()
# # # print(s1.color)



# # # # # # # Hybrid Level Inheritance
# # # class Shape:
# # #     color = "red"

# # # class Triangle(Shape):
# # #     sides = 3

# # # t1 = Triangle()
# # # print(t1.color)

# # # class Square(Shape):
# # #     sides = 4

# # # s1 = Square()
# # # print(s1.color)

# # # class Isosceles(Triangle):
# # #     degree = 180

# # # i1 = Isosceles
# # # print(i1.color)



# # class Mom:
# #     gender = "Female"

# # class Dad:
# #     gender = "Male"

# # class Me(Dad, Mom):
# #     sex = "M"

# # m1 = Me()
# # print(m1.gender)


# class Employee:

#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.department = dept
#         self.salary = salary

#     def showDetails(self):
#         print(f"Role = {self.role}")
#         print(f"Department = {self.department}")
#         print(f"Salary = {self.salary}")
#         print("----------------------------")

# e1 = Employee("Trainer", "IT", 999)
# # e1.showDetails()

# class Engineer(Employee):

#     def __init__(self, name, age, role, dept, salary):
#         self.name = name
#         self.age = age

#         # Employee().__init__(role, dept, salary)
#         super().__init__(role, dept, salary)

#     def showDetails(self):
#         print(f'Name = {self.name}')
#         print(f'Age = {self.age}')
#         super().showDetails()

#         # return "ABcD"


# eng1 = Engineer("Shivam", 99, "Technical Trainer", "B.Com", 9999)
# print(eng1.showDetails())


