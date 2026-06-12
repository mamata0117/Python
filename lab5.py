# 1.Write a Python  program to convert a tuple to a string. 
tuple1 =('p', 'y', 't', 'h','o', 'n')
print("Original tuple:", tuple1)
str1 = ''.join(tuple1)
print("After conversion to string:", str1)
#2.Write a Python program to get the 4th element from the last element of a tuple. 
tuple2 = ('a', 'b', 'c', 'd', 'e')
print("The 4th element from the last element of the tuple is:", tuple2[-4])
#3.Write a Python program to find repeated items in a tuple. 
tuple3 =(1, 2, 3, 4, 5, 1, 2)
repeated_items = set([x for x in tuple3 if tuple3.count(x) > 1])
print(repeated_items)
#4.Write a Python program to replace the last value of tuples in a list. 
sample_list = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
new_list = [t[:-1] + (100,) for t in sample_list]
print(new_list)
# 5.Write a Python program to sort a tuple by its float element. 
sampletuple =[('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
sorted_tuple = sorted(sampletuple, key=lambda x: float(x[1]),reverse=True)
print(sorted_tuple)

#6.Write a Python program to convert a given string list to a tuple. 
original_string = "python 3.0"
converted_tuple = tuple(original_string)
print(converted_tuple)
# 7.Write a Python program to calculate the product, multiplying all the numbers in a given tuple. 
tuple1 = (4, 3, 2, 2, -1, 18)
product = 1
for x in tuple1:
    product *= x
print("Multiplying all the numbers of the tuple gives:", product)
tuple2 = (2, 4, 8, 8, 3, 2, 9)
product2 = 1
for x in tuple2:
    product2 *= x
print("Multiplying all the numbers of the tuple gives:", product2)
# 8Write a Python program to calculate the average value of the numbers in a given tuple of tuples. 

tuple3=((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))
average_values = []
for inner_tuple in tuple3:
    average = sum(inner_tuple) / len(inner_tuple)
    average_values.append(average)  
print("Average value:", average_values) 
tuple2=((1, 1, -5), (30, -15, 56), (81, -60, -39), (-10, 2, 3))
average_values = []
for t in tuple2:
    average_values.append(sum(t)/len(t))
print('Average values:', average_values)
# #9.Write a Python program to convert a given tuple of positive integers into an integer.  
integertuple = (1, 2, 3)
result = int(''.join(map(str, integertuple)))
print('Result:',result)
original_tuple = (10, 20, 40, 5, 70)
result = int(''.join(map(str, original_tuple)))
print('Result:',result)
#10.Write a Python program to compute the element-wise sum of given tuples.
tuple1=(1, 2, 3, 4) 
tuple2=(3, 5, 2, 1) 
tuple3=(2, 2, 3, 1) 
elementwise_sum = tuple(a + b + c for a, b, c in zip(tuple1, tuple2, tuple3))
print(elementwise_sum)

# 11.Write a Python program to compute the sum of all the elements of each tuple stored inside a list of tuples. 

list_of_tuples = [(1, 2), (2, 3), (3, 4)]
result=[sum(x)for x in list_of_tuples]
print("Sum of all the elements of each tuple stored inside the said list of tuples:", result)

original_list = [(1, 2, 6), (2, 3, -6), (3, 4), (2, 2, 2, 2)]
result = [sum(t) for t in original_list]
print("Sum of all the elements of each tuple stored inside the said list of tuples:", result)
 
# Sets 
# 12.	Write a Python program to create an intersection, a union, set difference and a symmetric difference of sets. Also find the length, maximum and minimum values in a set. 
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print('The intersection of set1 and set2 is:', set1 & set2)
print('The union of set1 and set2 is:', set1 | set2)
print('The difference of set1 and set2 is:', set1 - set2)
print('The symmetric difference of set1 and set2 is:', set1 ^ set2)
print('The length of set1 is:', len(set1))
print('The maximum value in set1 is:', max(set1))
print('The minimum value in set1 is:', min(set1))
# 13.	Write a Python program that finds all pairs of elements in a list whose sum is equal to a given value. 
nums=[1, 2, 3, 4, 5, 6]
target_sum = 7
pairs = set()
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target_sum:
            pairs.add((nums[i], nums[j]))   
print("Pairs of elements in the list whose sum is equal to", target_sum, ":", pairs)

# 14.	Write a Python program to find the longest common prefix of all strings. Use the Python set. 

words = ['python', 'pyramid', 'pythagoras', 'pyjamas']
prefix = words[0]
for word in words[1:]:
    while not word.startswith(prefix):
        prefix = prefix[:-1]

print("Longest common prefix:", prefix)
# 15.	Write a  Python program to find the two numbers whose product is maximum among all the pairs in a given list of numbers. Use the Python set. 
numbers = [1, 2, 3, 4, 5, 6]

max_product = float('-inf')
pair = ()

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        product = numbers[i] * numbers[j]

        if product > max_product:
            max_product = product
            pair = (numbers[i], numbers[j])

print("Pair with maximum product:",pair)
print("Maximum product:", max_product)