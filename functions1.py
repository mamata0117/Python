# def f1():
#     s = "I will be cool,smart,talented Engineer"

#     def f2():
#         print(s)

#     f2()

# f1()
#Recursive function
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
# print(factorial(4))
# print('Find the largest item from a given list using function')
# x={4,6,8,24,12,2}
# print('Maximum:', max(x))
# print('Minimum:', min(x))

#define a funcn that accepts radius and returns area of circle
# def area_of_circle(radius):
#     pi = 3.14
#     area = pi * radius ** 2
#     return area

# print('Area of circle with radius 5:', area_of_circle(5))
#wap to sum of all numbers in a list
# list=[1, 2, 3, 4, 5]
# def sum_of_list(lst):
#     total = 0
#     for num in lst:
#         total += num
#     return total

# print('Sum of list:', sum_of_list(list))
# # lambda
# greet_user = lambda name: print(f"Hello, {name}!")
# greet_user('Mamata')
# #using function
# def f(x):
#     return x * 2
# print('Result of function f(5):', f(5))
calc=lambda num:'Even number' if num%2==0 else 'Odd number'
print(calc(5))
#reduce fuction
from functools import reduce
each_items_costs=[100, 200, 300, 400]
total_cost=reduce(lambda x,y:x+y,each_items_costs)  
print('Total cost:', total_cost)

