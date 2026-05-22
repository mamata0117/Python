 #1
# a=input("Enter a string:")
# print( f"The length of the {a} is {len(a)}\n")
# #2
# l=int(input("Enter the length of the rectangle:"))
# b=int(input("Enter the breadth of the rectangle:"))
# area=l*b
# print(f"The area of rectangle with length {l} and breadth {b} is {area}\n") 
# #3
# a=input("Enter a string:")
# if len(a)<2:
#     print(" ")
# else:
#     result=a[0:2]+a[-2:]
#     print(result )

# 4
# string=input("Enter a string:")
# b=string[0]
# new_string=string.replace(b,'#')
# print("The new string is:",b+new_string[1:])
# #5 with import math
# import math
# r=float(input("Enter the radius of the circle:"))
# print(f"Area:{math.pi*r**2}\n Circumference:{2*math.pi*r}")
# #without import math
# r=float(input("Enter the radius of the circle:"))
# pi=3.14159
# print(f"Area:{pi*r**2}\n Circumference:{2*pi*r}")
# #6
# a=int(input("Enter a number:"))
# b=int(input("Enter a number:"))
# print(f"The sum of {a} and {b} is {a+b}")
# #7
# a=int(input("Enter a number:"))
# print(f"The square root of {a} is {a**0.5}")
# #8
# a=int(input("Enter value of  a :"))
# b=int(input("Enter value of  b :"))
# c=0.5*a*b
# print(f"The area of triangle with base {a} and height {b} is {c}")
# #9
# # import math
# a = float(input("Enter coefficient a: "))
# b = float(input("Enter coefficient b: "))
# c = float(input("Enter coefficient c: "))
# d = b**2 - 4*a*c
# if d > 0:
#     root1 = (-b + math.sqrt(d)) / (2*a)
#     root2 = (-b - math.sqrt(d)) / (2*a)
#     print("Two real and distinct roots are:\n Root 1= ", root1 and "Root 2= ", root2)


# elif d == 0:
#     root = -b / (2*a)
#     print("Two real and equal roots are:", root)

# else:
#     real_part = -b / (2*a)
#     imaginary_part = math.sqrt(-d) / (2*a)
#     print("Two complex roots are:")
#     print("Root 1 =", real_part, "+", imaginary_part, "i")
#     print("Root 2 =", real_part, "-", imaginary_part, "i")
# #10
# print("\n")
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# a,b=b,a
# print(f"After swapping: a={a}, b={b}")
# print("\n")

# #11
# import random
# num = random.randint(1, 100)
# print("Random number:", num)
# print("\n")
#12
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("Maximum number is:", max(a, b))