#write a python program to take a number from user and sum them until 0
# sum=0
# a=int(input("Enter a number :"))
# while a!=0:
#     num = int(input("Enter a number : "))
#     if num == 0:
#         break
#     sum += num
# print("The sum is:", sum,"\n")

#1 checking whether a character is consonant orvowel
# ch=input("Enter a character:")
# if ch in 'aeiouAEIOU':
#     print(f"{ch} is a vowel")
# else:
#     print(f"{ch} is a consonant")

#2wap to enter a number from user and print its absolute valueimport
# num = int(input("Enter a number: "))

# if num <= -1:
#     print("Absolute value =", -num)
# else:
#     print("Absolute value =", num)
# print("\n")
#3wap to print the follwoing
#3.1 4 9 16 25 36 49 64 81 100
# n=int(input("Enter a range:"))
# for i in range(1,n+1):
#     print(i**2,end=" ") 
# #3.2 1/1 2/4 3/9 4/16 5/25 6/36 7/49 8/64 9/81 10/100
# n=int(input("Enter a range:"))
# for i in range(1,n+1):
#     print(f"{i}/{i**2}",end=" ")
# print("\n")
# #3.3  1+2+3+4+5+6+7+8+9+10
# n=int(input("Enter a range:"))
# sum=0
# for i in range(1,n+1):
#     sum+=i
# print("Sum =", sum)

#4wap to enter a number from user and reverse it
# num1=int(input("Enter a number:"))
# reverse_num=0
# while num1>0:
#     digit=num1%10
#     reverse_num=reverse_num*10+digit
#     num1=num1//10
# print("The reversed number is:", reverse_num)
# print("\n")
#5 wap to enter a num from user and print sum of its individual digits
# num=int(input("Enter a number:"))
# sum=0
# while num>0:
#     digit=num%10
#     sum+=digit
#     num=num//10
 
# print("Sum of individual digits:", sum)
#6take and num and check if its palindrome or not
# num=int(input("Enter a number:"))
# original_num=num
# reverse=0
# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10
# if original_num == reverse:
#     print(f"{original_num} is a palindrome")
# else:
#     print(f"{original_num} is not a palindrome")
#7wap to enter a num and print its individual digits on seperate lines in order
# num = int(input("Enter a number: "))
# s = str(num)
# #where str is used to convert the number into string so that we can iterate through each digit and print it on a separate line
# for digit in s:
#     print(digit,"\n")
#8wap to enter a num and print its factorial
# num=int(input("Enter a number:"))
# factorial=1
# for i in range(1,num+1):
#     factorial*=i
# print(f"Factorial of {num} is {factorial} \n")
#9wap to take a limit from user and print fibonacci series upto that limit
# num=int(input("Enter a limit:"))    
# a,b=0,1
# while a<=num:
#     print(a,end=" ")
#     a,b=b,a+b
# print("\n")
#print pattern
# for i in range(1,6):
#     print("*"*i)
     