# 1. Write a Python program to print number from 1 to 10 using while loop
num=1
while num<=10:
    print(num)
    num+=1

# 2. Write a Python program to calculate the sum of first n natural numbers using a for loop
n=int(input("Enter a  number: "))
sum=0
for i in range(1, n+1):
    sum+=i
print("The sum of the first", n, "natural numbers is:", sum)

# 3. Write a Python program to display the multiplication table of a number using a while loop.
num=int(input("Enter a number: "))
i=1
while i<=10:
    print(f"{num} x {i} = {num*i}")
    i+=1

# 4. Write a Python program to print all even numbers between 1 and 100 using a for loop.
for i in range(1,101):
    if i%2==0:
        print(i,end=" ")

# 5. Write a Python program to simulate a do-while loop for password checking until the correct password is entered.
correct_password="password123"
while True:
    password=input("Enter the password: ")
    if password==correct_password:
        print("Access granted.")
        break
    else:
        print("Incorrect password. Try again.")   

# 6. Write a Python program to find the factorial of a number using a while loop.
num=int(input("Enter a number: "))
factorial=1
i=1
while i<=num:
    factorial*=i
    i+=1
print("The factorial of", num, "is:", factorial)

# 7. Write a Python program to iterate through a list of student names using a foreach style loop (for item in list).
students=["Alice", "Bob", "Charlie", "David"]
for student in students:
    print(student)

# 8. Write a Python program to print numbers from 1 to 20 but stop when the number 15 is encountered using the break
for i in range(1,21):
    if i==15:
        break
    print(i)


# 9. Write a Python program to print numbers from 1 to 20 but skip multiples of 3 using the continue statement.
i=1
while i<=20:
    if i%3==0:
        i+=1
        continue
    print(i, end=' ')
    i+=1

# 10. Write a Python program to search for a number in a list and terminate the loop when the number is found using break.
numbers=[1, 3, 5, 7, 9, 11]
search_num=int(input("Enter a number to search: "))
for num in numbers:
    if num==search_num:
        print("Number found in the list.")
        break
else:    print("Number not found in the list.")

# 11. Write a Python program to demonstrate the use of the pass statement inside an empty loop or conditional block

for i in range(5):
    if i%2==0:
        pass
    else:        print(i)


# 12.  Write a Python program to print a pyramid pattern using nested for loops
n=int(input("Enter the number of rows: "))
for i in range(1, n+1):
    print(' '*(n-i)+'* '*(i))

# 13. Write a Python program to count the number of digits in a number using a while loop
num=int(input("Enter a number: "))
count=0
while num>0:
    num=num//10
    count+=1
print("The number of digits is: ", count)


#  14. Write a Python program to reverse a number using a while loop.
num=int(input("Enter a number: "))
reversed_num=0
while num>0:
    digit=num%10
    reversed_num=reversed_num*10+digit
    num=num//10
print("The reversed number is: ",reversed_num)    

# 15. Write a Python program to print all pAlme numbers between 1 and 100 using nested loops.
for num in range(1, 101):
    is_palindrome=True
    str_num=str(num)
    for i in range(len(str_num)//2):
        if str_num[i]!=str_num[-(i+1)]:
            is_palindrome=False
            break
    if is_palindrome:
        print(num, end=' ')