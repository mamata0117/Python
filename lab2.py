# #1
# num=int(input("Enter a number:"))
# sub=num-17
# if num>17 :
#     print(f"Difference : ",2*sub,"\n")
# else:
#     print("The number is less than 17 \n")
#2
# num=int(input("Enter a number :"))
# calc=num%2
# if calc==0:
#     print(f"{num} is even\n")
# else:
#      print(f"{num} is odd\n")   
#3wap to count the number 4 in given list
# data=[1,2,3,4,5,6,7,8,9,10,4,4]
# count=0
# for i in data:
#     if i==4:
#         count+=1
# print(f"The number 4 appears {count} times in the list \n")

# 4 
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# print(f"The number before swapping are {a} and {b}")
# a,b=b,a
# print(f"The number after swapping are  {a} and {b}")
# print("\n")
#5 check whether a variable is int,string,list,tuple or set
# a={1,2,3}
# if(type(a)==int):
#   print(f"{a} is a integer\n")
# if(type(a)==str):
#   print(f"{a} is a string\n")
# elif(type(a)==list):
#  print(f"{a} is a list\n")
# elif(type(a)==tuple):
#   print(f"{a} is a tuple\n")
# elif(type(a)==set):
#   print(f"{a} is a set\n")
#6 python script that takes two number as input  and prints their sum and difference,product and quotient
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# print(f"The sum of {a} and {b} is {a+b}")
# print(f"The difference between {a} and {b} is {a-b}")
# print(f"The product of {a} and {b} is {a*b}")
# if b != 0:
#     print(f"The quotient of {a} and {b} is {a/b}")
# else:
#     print(" Division by zero is not allowed.")
#7take an input from user then reverse the string using slicing
# data=input("Enter a string:")
# print(f"Reversed string: {data[::-1]}")
#8write a code to take input from the user and  store it in a variable spam then print hello  if 1 is stored in spam,print hi if 2 is stored in spam and print Greeting! if anything else is stored in spam
# var=int(input("Enter a variable to store in spam:"))
# if var==1:
#     print("Hello")
# elif var==2:
#     print("Hi")
# else:
#     print("Greeting!")
#9 python script that takes two number as input  and prints their sum and difference,product and quotient using match case
# n1=int(input("Enter first number:"))
# n2=int(input("Enter second number:"))
# operation=input("Enter the operation you want to perform sum, difference, product, quotient:")
# match operation:
#     case "sum":
#         print(f"The sum of {n1} and {n2} is {n1 + n2}")
#     case "difference":
#         print(f"The difference between {n1} and {n2} is {n1 - n2}")
#     case "product":
#         print(f"The product of {n1} and {n2} is {n1 * n2}")
#     case "quotient":
#         if n2 != 0:
#             print(f"The quotient of {n1} and {n2} is {n1 / n2}")
#         else:
#             print("Division by zero is not allowed.")
#     case _:
#         print("Invalid operation.")
#10 ask user for name and age ,then print a message that tells them in which year they'll turn 100 years old
# name=input("Enter your name: ")
# age=int(input("Enter your age: "))
# current_year=2026
# years_left=100-age
# if years_left>0:
#     year_turn_100=current_year+years_left
#     print(f"Hello {name}, you will turn 100 in the year {year_turn_100}.")
#11covert temp from fahrenheit to celsius and vice versa
# temp=float(input("Enter the temperature: "))
# unit=int(input("Enter the unit of temperature \n 1.Fahreneit \n 2.Celsius \n"))
# if unit==1:
#     print(f"{temp} degree Fahrenheit is equal to {(temp-32)*5/9} degree Celsius")
# elif unit==2:    
#     print(f"{temp} degree Celsius is equal to {(temp*9/5)+32} degree Fahrenheit")
#12child,teenager or adult based on age
# age=int(input("Enter your age :"))
# if age<12:
#     print("Child \n")
# elif  13<=age<=19:
#     print("Teenager \n")    
# else:
#     print("Adult \n")    
#13 take A,B,C,D,F as input and print the corresponding grade A=4.0, B=3.0, C=2.0, D=1.0, F=0.0 .Include if else to handle  invalid inputs
# grade=input("Enter your grade A, B, C, D, F: ")
# if grade=="A":
#     print("Your grade point is 4.0 \n")
# elif grade=="B": 
#     print("Your grade point is 3.0 \n")   
# elif grade=="C":
#     print("Your grade point is 2.0 \n")    
# elif grade=="D":
#     print("Your grade point is 1.0 \n")
# elif grade=="F":
#     print("Your grade point is 0.0 \n")
# else:
#     print("Invalid grade entered.\n")
#14take a num as input and print whether it's odd,even , zero or invalid for non-integer inputs,program shall check i/p is valid int or not and then only other
# num=int(input("Enter a number: "))
# if(type(num)==int):
#     if num==0:
#         print("The number is zero \n")
#     elif num%2==0:
#         print(f"{num} is even \n")
#     else:
#         print(f"{num} is odd \n")

#15 leap year 3 condition divisible by 4 and not divisible by 100 or divisible by 400 ,if leap year return boolean value true else false
# year=int(input("Enter a year: "))
# bool_leapYear = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# print(bool_leapYear)

