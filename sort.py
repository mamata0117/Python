#1 print a list of alphabets in ascending order
# strs=['Python','Code','Java','ROR']
# strs.sort()
# print(strs)
# strs=['python','code','java']
# strs.sort()
# print(strs)
#2 Creating a list
# counting=[4,1,5,2,3]
# print(sorted(counting))
# print(counting)
# counting.sort()
# print(counting)
# sorted doesnt change the original value but  .sort() makes change in original value
# print('Descending order')
# counting=[4,1,5,2,3]
# print('The original value is',counting)
# print('The sorted value is',sorted(counting))
# print('The reverse/descending value is',sorted(counting,reverse=True))
#3string sorting
# x='python'
# print(sorted(x))
# print('For tuples')
# x={'q','u','e','r','t','y'}
# print(sorted(x))


# print('Slicing of elements')
# i=['a','b','c','d','e','f','g']
# print(i[1:4])
# print(i[:4])
# print(i[1:])
# print(i[:])
# print('slicing with positive and negative index')
# print(i[-5:-2])
# print('slicing with step')
# print(i[1:6:2])
# print('Reversing a list')
# print(i[::-1])
# print('using slice function')
# slice_object=slice(1,4)
# print(i[slice_object])


# print('copying a list\n we can use \n 1.copy() method \n 2.slicing \n 3.list() function \n 4.copy module')
# print('1.Using copy() method')
# bags=['bag1','bag2','bag3']
# new_bags=bags.copy()
# print(new_bags)
# print('2.Using slicing')
# bags=['bag1','bag2','bag3', 'bag4']
# new_bags=bags[::]
# print(new_bags)
# print('3.Using list() function')
# bags=['bag1','bag2','bag3', 'bag4']
# new_bags=list(bags)
# print(new_bags)
# print('4.Using copy module')
# import copy
# bags=['bag1','bag2','bag3', 'bag4']
# new_bags=copy.copy(bags)
# print(new_bags)

# clothes=['shirt','pant','t-shirt','jeans']
# x=clothes.count('shirt')
# print(x)
# finding the maximum and minimum value in a list
numbers=[5,20,9,91,77]
numbers.sort()
print('The maximum value in the list is:',numbers[-1])
print('The minimum value in the list is:',numbers[0])
numbers=[15,20,9,891,77]
print('The maximum value in the list is:',max(numbers))
print('The minimum value in the list is:',min(numbers))
# without using sort you can usen max() and min()
