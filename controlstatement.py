# #1 Write a Python Program to print numbers from 1 to 10 using a while loop. 
# i = 1
# while i <= 10:
#     print(i)
#     i += 1
# #2 Write a Python Program to calculate the sum of first n natural numbers using a for loop.
# # Program to calculate the sum of first n natural numbers
# n = int(input("Enter a number: "))

# sum = 0

# for i in range(1, n + 1):
#     sum = sum + i

# print("Sum of first", n, "natural numbers is:", sum)
#3 Write a Python Program to display the multiplication table of a given number using a while loop.
# number = int(input("Enter a number: "))
# i = 1
# while i <= 10:
#     print(number, "x", i, "=", number * i)
#     i += 1
# #4 Write a Python Program to print all even numbers between 1 and 100 using for loop   
# for num in range(1, 101):
#     if num % 2 == 0:
#         print(num,end=" ")
# print()  # for a new line after printing all even numbers        
# #5 WAP to simulate a do-while loop for password checking until the correct password is entered.
# correct_password = "python123"

# while True:
#     password = input("Enter password: ")

#     if password == correct_password:
#         print("Correct password! Access granted.")
#         break
#     else:
#         print("Wrong password! Try again.")
# #6 WAP to find factorial of a number using a while loop.
# number = int(input("Enter a number: "))
# factorial = 1   
# i = 1
# while i <= number:
#     factorial *= i
#     i += 1  
# print("Factorial of", number, "is", factorial)
# #7Write a Python program to iterate through a list of student names using a foreach style loop (for item in list).
# students = ["Asha", "Rahul", "Priya", "Kiran"]
# for name in students:
#     print(name)
# #8  Write a Python program to print numbers from 1 to 20 but stop when the number 15 is encountered using the break statement.  
# for i in range(1, 21):
#     if i == 15:
#         break
#     print(i)
# #9Write a Python program to print numbers from 1 to 20 but skip multiples of 3 using the continue statement.
# for i in range(1, 21):
#     if i % 3 == 0:
#         continue
#     print(i)
# #10 Write a Python program to search for a number in a list and terminate the loop when the number is found using break.
# numbers = [10, 25, 30, 45, 50]
# search = 30
# for num in numbers:
#     if num == search:
#         print("Number found:", num)
#         break
# 11 Write a Python program to demonstrate the use of the pass statement inside an empty loop or conditional block.  
# for i in range(5):
#     pass
# print("Loop executed using pass statement")  
# #12Write a Python program to print a pyramid pattern using nested for loops.
# rows = 5
# for i in range(1, rows + 1):
#     for j in range(rows - i):
#         print(" ", end="")

#     for k in range(i):
#         print("* ", end="")
#     print()
# # 13 Write a Python program to count the number of digits in a number using a while loop.
# num = int(input("Enter a number: "))
# count = 0
# while num > 0:
#     num = num // 10
#     count += 1
# print("Number of digits:", count)
# # 14 Write a Python program to reverse a number using a while loop. 
# num = int(input("Enter a number: "))
# reverse = 0
# while num > 0:
#     digit = num % 10
#     reverse = reverse * 10 + digit
#     num = num // 10
# print("Reversed number:", reverse)
# 15 Write a Python program to print all prime numbers between 1 and 100 using nested loops.
# for num in range(2, 101):
#     prime = True

#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break

#     if prime:
#         print(num,end=" ")
# print()  
#16 Write a Python program to display Fibonacci series up to n terms using a for loop. 
# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# print("Fibonacci Series:")

# for i in range(n):
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
# print()    
# #17 Write a Python program to continuously ask the user for numbers and stop only when the user enters 0 using a loop and break.
# while True:
#     num = int(input("Enter a number: "))

#     if num == 0:
#         print("Program stopped")
#         break

#     print("You entered:", num)
# print()
# # 18 Write a Python program to print all characters of a string except vowels using a for loop and continue statement.
text = input("Enter a string: ")

for ch in text:
    if ch.lower() in "aeiou":
        continue
    print(ch, end="")
print()
#19 Write a Python program to check whether a number is a palindrome using a while loop.
# num = int(input("Enter a number: "))

# temp = num
# reverse = 0

# while temp > 0:
#     digit = temp % 10
#     reverse = reverse * 10 + digit
#     temp = temp // 10

# if num == reverse:
#     print("Palindrome number")
# else:
#     print("Not a palindrome")
# print()
# 20 Write a Python program to print numbers from 1 to 50, skipping numbers divisible by both 2 and 5 using the continue statement.
for i in range(1, 51):

    if i % 2 == 0 and i % 5 == 0:
        continue

    print(i,end=" ")