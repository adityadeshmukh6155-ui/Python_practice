# number = 15

# if number %2 == 0:
#     print("even")
# else:
#     print("odd")
# ==================================================================================================


# salary = 60000

# if salary <= 50000:
#     print("bonus is 10%")

# else:
#     print("bonus is 5%")
# ==================================================================================================


# sales = [500, 1200, 800, 2000, 3000]

# high_sales =[]

# for sale in sales:
#    if sale > 1000:
#     high_sales.append(sale)

# print(high_sales)
# ==================================================================================================


# sales = [100, 200, 300, 400]

# total = 0

# for value in sales:
#     total += value

# print(total)
# ==================================================================================================


# sales = [500, 1200, 800, 2000]

# high_sales = sales[0]

# for value in sales:
#     if value > high_sales:
#      high_sales = value
# print(high_sales)
# ==================================================================================================


# customers = ["Ram", "John", "Ram", "Alex", "John"]
# duplicate = []

# for item in customers:
#       if item not in duplicate:
#          duplicate.append(item)

# print(duplicate)
# ==================================================================================================


# def calculate_total(price, quantity):

#     total = price * quantity

#     return total

# price = 100
# quantity = 5
#
# result = calculate_total(price, quantity)
# print("your total is",result)
# ==================================================================================================


# def clean_name(name):

#     return name.strip().capitalize()

# input = "aditya"
# clean_name = clean_name(input)
# print(input)
# ==================================================================================================


# employee = {
#     "name":"Aditya",
#     "department":"IT",
#     "salary":60000
# }

# print("employe name",employee["name"])
# print("employee department",employee["department"])
# print("employee salary",employee["salary"])
# ==================================================================================================


# text = "data engineering data python"
# words =text.split()
# frequency = {}

# for word in words:
#     if word in frequency:
#         frequency[word] += 1
#     else:
#         frequency[word] = 1

# for word,count in frequency.items():
#  print(f"{word}:{count}")
# ==================================================================================================


# with open("Python-Aditya/learning_files(input/output)/pract.txt","r") as f:
#     data = f.read()
#     print(data)
#     f.close
# ==================================================================================================

# import csv

# with open("Python-Aditya/learning_files(input/output)/pract.txt","r") as file:
#     reader  = csv.DictReader(file)
#     for row in reader:
#         if int(row["Salary"]) > 55000:
#             print(row["Name"])
# ===================================================================================================

# data = ("aditya prakash deshmukh")

# for data in data:
#     print(f"round : {data}")
# =====================================================================================================

# 7_table

# i = 0
# for num in range(7,72,7) :
#     i += 1
#     print(f"7 x {i} = {num}")

# or


# x = 7
# for i in range(1, 11):
#     print(f"7 x {i} = {x*i}")

# ===============================================================================================

# number = "+49 (176) 123-4567"
# print(number.replace("+","00").replace(" ","").replace("-","").replace("(","").replace(")",""))

# number = "+49 (176) 123-4567"
# print(number.replace("+49 (176) 123-4567","00491461234567"))
# ================================================================================================

# name = "aditya"
# name1 = "deshmukh"
# name2 = " "

# print(name + name2 +name1)
# ===============================================================================================

# name  = ("my name is aditya prakash/deshmukh ,27-04-1997,28,413+512")
# print(name.replace("+","").replace("/"," ").split(","))
# ===============================================================================================

# text = "968-Maria , ( Data engineer ) ;; 27y  "
# clean = text.replace("968","name").replace(",","|").replace(")","|").replace(";;"," age :").replace("(","role :").strip().replace("27y","27")
# print(clean)
# ===============================================================================================

# text = "968-Maria , ( Data engineer ) ;; 27y  "
# text = "968-Maria , ( Data engineer ) ;; 27y"

# clean = text.replace("968", "name")
# clean = clean.replace(",", "|")
# clean = clean.replace("(", "role :")
# clean = clean.replace(")", "")
# clean = clean.replace(";;", "| age :")
# clean = clean.replace("27y", "27")
# clean = clean.strip()
# print(clean)
# ===================================================================================================


# print("===== Python Calculator =====")
# print("Type your calculation like: 2+2, 10*5, 100/4")
# print("Type 'exit' to close calculator")

# while True:
#     calculation = input("\nEnter calculation: ")

#     if calculation == "exit":
#         print("Calculator closed")
#         break

#     try:
#         answer = eval(calculation)
#         print("Answer:", answer)

#     except:
#         print("Invalid calculation")
# ================================================================================================

# import random

# num = input(random.randint(1,100))
# num1 = num % 2 == 0

# print(num1)
# ================================================================================================

# cpu = 90
# gpu = 70
# total = not cpu > 90 or not gpu >  70
# print(total)
# =================================================================================================

# access = input("enter : you are user or guest or nothing   ")
# user = input("user enter your password   ")
# user_password = "Aditya"
# guest = ("guest enter your password   ")
# guest_password = "aditya"
# nothing = "you can not access   "

# if access == user:
#     print("user")
#     if user_password == user:
#         print("welcome the AC")
#     else:
#         print("error")

# elif access == guest:
#     print("guest") 
#     if guest == guest_password:
#         print ("weclome to dc")
#     else:
#         print("error")
# elif access == nothing:
#     print("you can access")
# =============================================================================================================

# access = input("Enter user or guest: ")

# user_password = "Aditya"
# guest_password = "aditya"

# if access == "user":
#     password = input("User, enter your password: ")

#     if password == user_password:
#         print("Welcome to AC")
#     else:
#         print("Error: Wrong password")

# elif access == "guest":
#     password = input("Guest, enter your password: ")

#     if password == guest_password:
#         print("Welcome to DC")
#     else:
#         print("Error: Wrong password")

# else:
#     print("You cannot access")
# ==================================================================================================

# access = "user" or "guest"

# print(input("enter   "))

# if "user" == "guest":
#     print("welcome")
# else:
#     print("u are not allowed here to access")
# =================================================================================================
# salary = float(input("Enter salary: "))

# if salary > 50000:
#     bonus = salary * 0.10
# else:
#     bonus = salary * 0.05

# total_salary = salary + bonus

# print("Bonus:", bonus)
# print("Total Salary:", total_salary)
# ================================================================================================

# age  = int(input("enter your age:  "))

# if age <= 18:
#     print("you are minor")
# elif age <=  60:
#     print("you are adult")
# else:
#     print("you are senoir ")
# ====================================================================================================

# age  = int(input("enter your age:  "))
# if age < 18:
#     print("You are a Minor")
# elif 18 <= age <= 60:
#     print("You are an Adult")
# else:
#     print("You are a Senior Citizen")
# =====================================================================================================

# age = int(input("Enter your age: "))

# if age < 18:
#     print("You are a Minor")
# elif age >= 18 and age <= 60:
#     print("You are an Adult")
# else:
#     print("You are a Senior Citizen")
# =======================================================================================================

# a  = int(input("inter your age "))
# b = input("inter your height ")
# c = input("inter your name ")
# d = input("are you student ")
# e = None

# print(len(a))
# print(len(b))
# print(len(c))
# print(len(d))
# print(e)

# =======================================================================================
# import math
# price = 35.15
# print(round(price,2))
# print(math.floor(price))

# x = 1.2
# print(x.is_string())

# Write a program that:
# Takes two numbers as input.
# Adds them.
# Prints the result.

# x = input("enter the value of x :")
# y = input("enter the value of y :")
# z  = x + y

# print(z)

# x = int(input("enter the value of x :"))
# y = int(input("enter the value of y :"))
# sum = x + y
# print("Addition of two numbers is", sum)


# Take two numbers and subtract the second from the first.
# x  = 24
# y = 12
# z = x*y
# print(z)

# Divide two numbers.
# If the second number is 0, print:

# x = 2
# y = 3
# char = ("/")
# if char != 0:
#     print("odd numer")
# else:
    
#     print("even number")

# x = 2
# y = 3

# if y == 0:
#     print("Cannot divide by zero")
# else:
#     print("Result =", x / y)


# Ask the user for:
# First number
# Operator (+, -, *, /)
# Second number

# num1 = float(input("enter yout first number : "))
# operator = input(" enter your oprtaror (+, -, *, /) : ")
# num2 = float(input("enter yout second number : "))

# if operator == "+":
#     print("result : ", num1 + num2) 
# elif operator == "-":
#     print("result : ", num1 - num2)
# elif operator == "*":
#     print("result : ", num1 * num2)
# elif operator == "/":
#     if num2 == 0:
#         print("we cant divide by 0")
#     else:
#         print("result : " ,num1 / num2)
    
# else:
#     print("error")

# =========================================================================================
# Next Challenge (Level Up)
# Add these three operators:
# % (Modulus)
# ** (Power)
# // (Floor Division)

# num1 = float(input("enter yout first number : "))
# operator = input(" enter your oprtaror (%, **, //) : ")
# num2 = float(input("enter yout second number : "))

# if operator == "%":
#     print("result : ", num1 % num2) 
# elif operator == "**":
#      print("result : ", num1 ** num2)
# elif operator == "//":
#      print("result : ", num1 // num2)
   
# else:
#      print("error")


#  PYTHON CALCULATOR
# ============================
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# 4. Division
# 5. Modulus
# 6. Power
# 7. Floor Division
# 8. Exit
# ============================
# Enter your choice:

# print("welcome to the calculator")


# num1 = float(input("enter yout first number : "))
# operator = input(" enter your oprtaror (%, **, //,+, -, *, /) : ")
# num2 = float(input("enter yout second number : "))

# if operator == "%":
#     print("result : ", num1 % num2) 
# elif operator == "**":
#      print("result : ", num1 ** num2)
# elif operator == "//":
#      if num2 == 0:
#              print("we cant divide by 0")
#      print("result : ", num1 // num2)
# elif operator == "+":
#     print("result : ", num1 + num2) 
# elif operator == "-":
#     print("result : ", num1 - num2)
# elif operator == "*":
#     print("result : ", num1 * num2)
# elif operator == "/":
#     if num2 == 0:
#         print("we cant divide by 0")
#     else:
#         print("result", num1 / num2)

   
# else:
#      print("error")

# ==========================

# while True:

#     print("\n====== PYTHON CALCULATOR ======")
#     print("1. Addition")
#     print("2. Subtraction")
#     print("3. Multiplication")
#     print("4. Division")
#     print("5. Modulus")
#     print("6. Power")
#     print("7. Floor Division")
#     print("8. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "8":
#         print("Thank you for using the calculator!")
#         break

#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))

#     if choice == "1":
#         print("Result =", num1 + num2)

#     elif choice == "2":
#         print("Result =", num1 - num2)

#     elif choice == "3":
#         print("Result =", num1 * num2)

#     elif choice == "4":
#         if num2 == 0:
#             print("Cannot divide by zero")
#         else:
#             print("Result =", num1 / num2)

#     elif choice == "5":
#         if num2 == 0:
#             print("Cannot divide by zero")
#         else:
#             print("Result =", num1 % num2)

#     elif choice == "6":
#         print("Result =", num1 ** num2)

#     elif choice == "7":
#         if num2 == 0:
#             print("Cannot divide by zero")
#         else:
#             print("Result =", num1 // num2)

#     else:
#         print("Invalid choice")

#     again = input("Do you want to continue? (y/n): ")

#     if again.lower() == "n":
#         print("Goodbye!")
#         break

# ==============================================================================

# Even or Odd
# Ask the user to enter a number.
# If the number is even, print:

# num1 = float(input("enter your number  :"))


# if num1 % 2 == 0:
#     print("even number" )
# else:
#     print("odd number")


# Find the Largest of Three Numbers
# Write a program that asks the user to enter three numbers and prints the largest one.

# x = int(input("enter your number  "))
# y = int(input("enter your number  "))
# z = int(input("enter your number  "))

# if  x >= y and x >= z:
#     print(" largest number is  ",x )
# elif y >= x and y >= z:
#     print("largest number is : ",y)
# else: 
#     print("largest number is  :" ,z)

# =====================================================================================

# Write a program to determine whether a year is a Leap Year.
# Examples

# year= int(input("enter your year "))

# if (year % 4 == 0):
#     print("this is leap year", year)
# else:
#     print("this is not leap year")


# Question 5: Grade Calculator
# Write a program that asks the user to enter their marks (0–100) and prints the grade.

# marks =  int(input("enter your marks : "))

# if marks >= 90   :
#     print("A" , marks)
# elif marks >= 80 or marks <= 71:
#     print("B ") 
# elif marks >= 70:
#     print("c") 
# elif marks >= 60:
#     print("c ") 
# elif marks >= 50:
#     print("d ") 
# elif marks >= 40:
#     print("e ") 
# else:
#     print("fail")

# ========================================================================

# Reverse a Number
# Example:Enter a number: 12345
# Reverse = 54321

num1 = int(input("enter your number"))

while True:
    if num1 % 10 == 0:
      print("result : " , num1)
      break
    elif num1 // 10 == 0:
       print("result : " ,num1)
       break
    else:
       print("error")
       break
      
      
