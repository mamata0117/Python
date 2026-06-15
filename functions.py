# def cart(item,price=100):
#     print(f"The price of {item} is {price}")
# cart(item='pen')
# cart(item='handbag',price=15000)
# cart(price=5000,item='laptop')
# print()

# #2py program to demonstarte keyword arguments
# def student(firstname,lastname):
#     print(f"The name of the student is {firstname} {lastname}") 
# student(firstname='John',lastname='Denver')
# student(lastname='Smith',firstname='Will')
# student('Alice','Johnson')
# student('Bob',lastname='Brown')
# student(lastname=input('lname:'),firstname=input('fname:'))
# #3
# def my_function(child3, child2, child1):
#     print("The youngest child is " , child3)
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 
# #4 keyword only arguments
# def my_function(*,x):
#     print(x)
# my_function(x=10)   
'''* is used to indicate that the following parameters are keyword-only arguments,
meaning they must be specified using their parameter name when calling the function. In this case, x is a keyword-only argument, and you must call the function with x=10 to provide a value for it.'''
# def my_function(X):
#     print(X)
# my_function(11)

# def sumation(*,x,y):
#     print("sum is",x+y)
# sumation(x=9,y=5)
# what if i want  only x to be keyword argument and y to be positional argument?
# # You can achieve that by defining the function with a combination of positional and keyword arguments. Here's how you can modify the `sumation` function to make `x` a keyword argument and `y` a positional argument:
# def test(x, y):
#     print("sum is", x + y)
# test(5, y=10)  # This will work, x is positional and y is keyword
# test(y=10, x=5)  # This will also work, x is keyword

#calling funcn and passing arguments 20 and 30
# def function(n1,n2):
#    print('N1 is',n1)
#    print('N2 is',n2)
# print("passing arguments 20 and 30:")
# function(20, 30)
# #for position only
# def my_function(x, /):
#     print(x)
# my_function(10)  # This will work
# # my_function(x=10)  # This will raise a TypeError because x is a positional-only argument
# def my_function(x, y, /):
#     print(x, y)
# my_function(10, 20)  # This will work
# # my_function(x=10, y=20)  # This will raise a TypeError because x and y are positional-only arguments
# # keyword-only arguments
# def my_function(*, x, y):
#     print(x, y)
# my_function(x=10, y=20)  # This will work
# # my_function(10, 20)  # This will raise a TypeError because x
# # for position and keyword arguments
# def my_function(x, y, /, z):
#     print(x, y, z)
# my_function(10, 20, z=30)  # This will work
# # my_function(x=10, y=20, z=30)  # This will raise a TypeError because x and y are positional-only arguments
# # combine position only and keyword-only arguments
# def my_function(x, y, /, *, z):
#     print(x, y, z)
# my_function(10, 20, z=30)  # This will work
# # my_function(x=10, y=20, z=30)  # This will raise a TypeError because x and y are positional-only arguments
# def my_function(x, y, /,*, z, w):
#     print(x, y, z, w)   
# my_function(10, 20, z=30, w=40)  # This will work
# # my_function(x=10, y=20, z=30, w=40)  # This will raise a TypeError because x and y are positional-only arguments
# Arbitary arguments are used in Python to allow a function to accept an arbitrary number of arguments. This is done using the *args and **kwargs syntax. This is used when  programmers are not sure about the number of arguments that will be passed to a function.
# *args is a non keyword argument that allows a function to accept any number of positional arguments. It is represented by an asterisk (*) followed by a variable name (commonly args). The arguments passed to the function are collected into a tuple.
# print("Arbitrary positional arguments using *args:")
# def my_function(*numbers):
#     print("The numbers are:", numbers)
# my_function(1, 2, 3, 4, 5)
# print('Another example of *args:')
# def sum_all(*numbers):
#     return sum(numbers)
# print(sum_all(1, 2, 3)) 
# print(sum_all(4, 5, 6, 7))  
    
# def total_cost(x,*y):
#     sum=0
#     for i in y:
#         sum+=i
#     print("Total cost is",x+sum)
# total_cost(100, 20)
# total_cost(100, 20, 30, 50)
# total_cost(100)
#double ** is used to pass a variable number of keyword arguments to a function. It allows you to pass a dictionary of key-value pairs as arguments to the function. The keys in the dictionary become the parameter names, and the values become the corresponding argument values.
# def my_function(**kid):
#         print("The last name of the kid is " + kid["lname"])
# my_function(fname="Tobias", lname="Refsnes")
# def greet(**words):
#         for key,value in words.items():
#             print(f"{key}: {value}")    
# greet(greeting="Hello", name="Alice", age=30)
def myfun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
myfun(first='Geeks', mid='for', last='Geeks')