# #1wap to check whether a num is positive,negative or zero using simple if statement
# num = int(input("Enter a number: "))

# if num < 0:
#     print(f"{num} is negative")

# elif num > 0:
#     print(f"{num} is positive")

# else:
#     print(f"{num} is zero")
# print("\n")
# #2wa python program to determine whether a student has passed or failed based on marks entered by user using if else  
# marks = int(input("Enter your marks: "))

# if marks >= 40:
#     print("Student has passed\n")
# else:
#     print("Student has failed\n")
# #3checking odd/even using conditional statements
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print(f"{num} is Even\n")
# else:
#     print(f"{num} is Odd\n")
# #4find the largest of two number using if else
# num1=int(input("Enter a number1:"))
# num2=int(input("Enter a number2:"))
# if num1>num2:
#     print(f"{num1} is largest\n")
# else:
#     print(f"{num2} is largest\n")
# #5wap to check whether a person is eligible to vote or not
# age=int(input("Enter your age:"))
# if age>=18:
#     print("You are eligible to vote\n")
# else:
#     print("You are not eligible to vote\n")

# #6wap to calculate bonus
# #salary above 50000 get 10% bonus,else 5% bonus
# salary=int(input("Enter your salary:"))
# if salary>50000:
#     bonus=0.1*salary
#     print(f"Your bonus is {bonus}\n")
# else:
#     bonus=0.05*salary
#     print(f"Your bonus is {bonus}\n")
# #7 to find great among 3 num using if else 
# num1=int(input("Enter num1: "))
# num2=int(input("Enter num2: "))
# num3=int(input("Enter num3: "))
# if num1>num2 and num1>num3:
#     print(f"{num1} is greatest\n")
# elif num2>num1 and num2>num3:    
#     print(f"{num2} is greatest\n")
# else:
#     print(f"{num3} is greatest\n")    
# #8 display grade  90 and above A,80-89 B,70-79 C,60-69 D,below 60 F
# marks=int(input("Enter your marks: "))
# if marks>=90:
#     print("Your grade is A")
# elif marks>=80 and marks<=89:
#     print("Your grade is B")
# elif marks>=70 and marks<=79:
#     print("Your grade is C")
# elif marks>=60 and marks<=69:
#     print("Your grade is D")
# else:
#     print("Your grade is F")
# print("\n")
# #9 determine whether a year is leap year or not
# year=int(input("Enter a year: "))
# if year % 4 == 0:
#     print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")
# print("\n")
# #10 check whether a character entered by user is vowel or consonant
# char=input("Enter a character: ")
# if char in 'aeiouAEIOU':
#     print(f"{char} is a vowel")
# else:
#     print(f"{char} is a consonant")
# print("\n")
# #11calculator using if elif else for addition,subtraction,multiplication and division
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# operation = input("Enter operation +, -, *, /: ")
# if operation == "+":
#   print(f"Result: {num1+num2}")
# elif operation == "-":
#   print(f"Result: {num1 - num2}")
# elif operation == "*":
#     print(f"Result: {num1 * num2}")
# elif operation == "/":
#     if num2 != 0:
#       print(f"Result: {num1 / num2}")
#     else:
#         print(" Division by zero is not allowed.")
# else:
#     print("Invalid operation.")
# print("\n")
# #12 determine type of triangle based on sides entered by user
# side1 = float(input("Enter the length of the first side: "))
# side2 = float(input("Enter the length of the second side: "))
# side3 = float(input("Enter the length of the third side: "))
# if side1 == side2 == side3:
#     print("The triangle is equilateral.\n")
# elif side1 == side2 or side2 == side3 or side1 == side3:
#     print("The triangle is isosceles.\n")
# else:
#     print("The triangle is scalene.\n")
# #13check whether num is divisible by both 5 and 11 or not
# num = int(input("Enter a number: "))
# if num % 5 == 0 and num % 11 == 0:
#     print(f"{num} is divisible by both 5 and 11\n")
# else:
#     print(f"{num} is not divisible by both 5 and 11\n")
# #14wap to check whether a person can get driving license or not based on age and vision test
# age=int(input("Enter your age: "))
# vision_test=input("Have you passed the vision test? (yes/no): ")
# if age >= 18 and vision_test.lower() == "yes":
#      print("You are eligible for a driving license.\n")
# else:
#      print("You are not eligible for a driving license.\n")
# #15wap to classify temp below 0 as freezing,0-15 as cold,16-30 as warm,above 30 as hot     
# temperature = float(input("Enter the temperature: "))
# if temperature < 0:
#     print("The temperature is freezing.\n")
# elif temperature <= 15:
#     print("The temperature is cold.\n")
# elif temperature <= 30:
#     print("The temperature is warm.\n")
# else:
#     print("The temperature is hot.\n")
#16check login credentials  using username and password with nested conditions
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin":
    if password == "password123":
        print("Login successful.\n")
    else:
        print("Incorrect password.\n")
#17calc electricity bill based on units consumed using multiple elif blocks
# units=float(input("Enter the number of units consumed: "))
# if units <= 100:
#     bill = units * 0.5
# elif units <= 200:
#     bill = 100 * 0.5 + (units - 100) * 0.75
# elif units <= 300:
#     bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.20
# else:
#     bill = 100 * 0.5 + 100 * 0.75 + 100 * 1.20 + (units - 300) * 1.50
# print(f"Your electricity bill is: {bill:.2f}\n")
# #18menu driven system using python match case  area of circle,rectangle and triangle
# operation=int(input("Enter the shape you want to calculate area for \n 1.Circle \n 2.Rectangle \n 3.Triangle \n"))
# match operation:
#     case 1:
#         radius=float(input("Enter the radius of the circle: "))
#         area=3.14159*radius**2
#         print(f"The area of the circle is: {area:.2f}")
#     case 2:
#         length=float(input("Enter the length of the rectangle: "))
#         width=float(input("Enter the width of the rectangle: "))
#         area=length*width
#         print(f"The area of the rectangle is: {area:.2f}")
#     case 3:
#         base=float(input("Enter the base of the triangle: "))
#         height=float(input("Enter the height of the triangle: "))
#         area=0.5*base*height
#         print(f"The area of the triangle is: {area:.2f}")
#     case _:
#         print("Invalid option.\n")
# print("\n")  
# #19 use match case to display the day name based on day number entered by user
# daynum=int(input("Enter a day number 1-7: "))
# match daynum:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("Invalid day number.")
#20use match case to perform arithmetic operations based on operator entered by user
operator=input("Enter the operator you want to perform +, -, *, /: ")
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))
match operator:
    case "+":
        print(f"Result: {num1 + num2}")
    case "-":    
        print(f"Result: {num1 - num2}")
    case "*":   
        print(f"Result: {num1 * num2}")
    case "/":
        if num2 != 0:
            print(f"Result: {num1 / num2}")
        else:
            print("Division by zero is not allowed.")
    case _:
        print("Invalid operator.")
print("\n")
