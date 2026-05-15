#1 Print even ibers from 0 to 10
'''for i in range(0, 11):
    if i % 2 == 0:
        print(i)
    else:
        pass

print("Odd ibers from 0 to 12:")
for i in range(1, 13):
    if i % 2 != 0:
        print(i)
    else:
        pass '''

# use # or ''' to comment out code that you don't want to run, but want to keep for reference.
#2 to print the result of integer division and float division
'''a,b=20,5
c,d=14.5,4.30
print(f"The result of integer division of {a} by {b} is {a//b}")
print(f"The result of float division of {c} by {d} is {c/d}")'''
#3evaluate the following expressions
'''print(4*(6+5))
print(4*6+5)
print(4+6*5)
print(5>4 and 3==5) 
print(not (5>4))
print(5>4 or 3==5)
print(not (5>4) or (3==5))
print((True and True ) and (True==False))
print((not False) or (not True))

#4
print(f"The result of expression 3*1.5+4 is type {type(3*1.5+4)}") '''
'''#5
num=int(input("Enter a number:"))
print(f"The square of the num is {num**2} and square root of the num is {num**0.5}")
# or
a=2
print(f"The square of the num is {a**2} and square root of the num is {a**0.5}")
# unlike in c++ we cant use num^2 to get the square of the num, we have to use num**2 instead.'''
'''#6
data1=80
data2=90.005
data3="MATH"
print(f"The type of data1 is {type(data1)}")
print(f"The type of data2 is {type(data2)}")
print(f"The type of data3 is {type(data3)}")'''

'''#7 testing whether the following variables is list,tuple or set
#  a=(1,2,3)is tuple {1,2,3} is set [1,2,3] is list
a=(1,2,3)
if (type(a)==list):
    print("a is a list")
elif (type(a)==tuple):
    print("a is a tuple")
else:
    if(type(a)==set):
        print("a is a set")
         #if elif elif else is used to test multiple conditions '''
   #8 
'''print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are!")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are")'''
'''#9checking the version of python you are using
import sys
print(f"You are using python version {sys.version}")'''

'''#10 to display first and last colors in the following list
color_list=["Red","Green","White","Black","Blue"]
print(f"First color: {color_list[0]}")
print(f"Last color:  {color_list[4]}")
#11vol of sphere with radius 6
import math
radius=6
volume=(4/3)*math.pi*radius**3
print(f"The volume of the sphere with radius {radius} is {volume}")
#12
a,b,c=3,3,3
if(a!=b and b!=c and a!=c):
 print(f"The sum of {a,b,c} is {a+b+c}")
else:
  if(a==b and b==c and c==a):
     print(f"The sum of {a,b,c} is {3*(a+b+c)}")'''
'''#13
a=17
b=20
if(15<=a<=20 and 15<=b<=20):
    print(f"The sum of {a} and {b} is 20")

else:
   print(f"The sum of {a} and {b} is {a+b}")
#15
x,y=4,3
print(f"({x}+{y})^2 = {(x+y)*(x+y)}")'''
'''
#16
n=3
result=" " 
for i in range(n):
   data=input("Enter a string: ")
   result+=data+" "
print(result)

#17
x,y=30,20
print(f"{x}+{y}={x+y}") 
#18
a=10
b='hello'
c=3.14
print(f"The type of a is {type(a)}")
print(f"The type of b is {type(b)}")
print(f"The type of c is {type(c)}")'
 #19
name=input("Enter your name:")
print(f"Hello {name}, welcome to python programming!")
#20
roses=input("Enter the number of roses you want to buy:")
roses=int(roses)
print("You have",roses,"roses in your cart")'''