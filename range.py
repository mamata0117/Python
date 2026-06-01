# numbers=list(range(1, 10))
# print("The numbers from 1 to 9 are:", numbers)
# even_numbers=list(range(2, 11, 2))
# print("The even numbers from 1 to 10 are:", even_numbers)
# odd_numbers=list(range(1, 10, 2))
# print("The odd numbers from 1 to 9 are:", odd_numbers)
# reverse_numbers=list(range(10, 0, -1))
# print("The numbers from 10 to 1 are:", reverse_numbers)
# fruits=['apple','banana','cherry']
# print("The fruits are:", fruits)
# print("The number of fruits is:", len(fruits))
# for i in range(len(fruits)):
#     print(fruits[i])
#directly using for loop
# fruits=['cherry','apple','banana','grape']
# for x in fruits:
#     print(x)
#  using while loop
# fruits=['cherry','apple','banana','grape']
# i=0
# while i < len(fruits):
#         print(fruits[i])
#         i += 1
# List comprehension
# animals=['cat','dog','rabbit']
# m=[x for x in animals]
# print(m)
#without using list comprehension
# animals=['cat','dog','rabbit']
# newlist=[]
# for x in animals:
#     if 'a'in x:
#      newlist.append(x)
#      print(newlist)
# for loop vs list comprehension
# list comprehension is generally more concise and faster than using a for loop to create a new list
# squares=[x**2 for x in range(1, 11)]
# print("The squares of numbers from 1 to 10 are:", squares)
# numbers=['1','2','3','4','5']
# square_numbers=[]
# #for loop to solve this
# for x in numbers:
#     square_numbers.append(int(x)**2)
#     print("The square of numbers from 1 to 5 are:", square_numbers)
# #using list comprehension   
# square_numbers=[int(x)**2 for x in numbers]
# print("The square of numbers from 1 to 5 are:", square_numbers)

#upper and lower
# names=['rAm','siTa','hAri']
# upper=[i.upper() for i in names]
# print(upper)
# lower=[i.lower() for i in upper]
# print(lower)
