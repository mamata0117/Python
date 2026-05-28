# emp=['Milan',102,'Nepal']
# Dep1=['CS',10]
# Dep2=['IT',11]
# HOD_CS=[10,'Mr.CS']
# HOD_IT=[11,'Mr.IT']
# print('printing employee data.....')
# print('Name:%s,ID:%d,Country:%s' % (emp[0], emp[1], emp[2]))
# print('printing department data.....')
# print('Department 1:\nName:%s,ID:%d\n Department 2:\nName:%s,ID:%d' % (Dep1[0], Dep1[1], Dep2[0], Dep2[1]))
# print('printing HOD data.....')
# print('CS HOD Name:%s,Id:%d' % (HOD_CS[1], HOD_CS[0]))
# print('IT HOD Name:%s,Id:%d' % (HOD_IT[1], HOD_IT[0]))
# print(type(emp),type(Dep1),type(Dep2),type(HOD_CS),type(HOD_IT))
# print('printing employee data.....')
# print('Name:%s,ID:%d,Country:%s' % (emp[0], emp[1], emp[2]))
# print('Name:{}'.format(emp[0]))
#multidimensional list
# List=[['Welcome','to'],['Python','Class']]
# print('Accessing a element from multidimensional list.....')
# print(List[0])
# print(List[0][0])
# print(List[1][1])
# List=[[[['Wel'],['come']],['to']],['Python','Class']]
# print('Accessing a element from multidimensional list.....')
# print(List[0])
# print(List[0][0])
# print(List[0][1])
# print(List[0][0][0])
# print(List[0][0][1])
# print(List[1][1])

print("List Operations and its Types")
List1=[1,2,3,4,5,6]
print(List1)
List1[2]=10
print(List1)
List1[1:3]=[80,70]
print(List1)
print('adding element in list\n 1.append()\n 2.insert()\n 3.extend()')
print('1.position,value')
fruits=['apple','banana','orange']
print('before append:',fruits)
fruits.append('grape')
fruits.append('melon')
print("We can't add multiple elements using append at one time 'grape' and 'melon' are added using two append statements")
print('after append:',fruits)
print('Append adds an element at the end of the list')
fruits.insert(1, 'kiwi')
print('after insert:',fruits)
print('Insert adds an element at a specific position')
fruits.extend(['mango','papaya'])
print('after extend:',fruits)
print('Extend adds multiple elements at the end of the list')
a=[1,2,3]
b=['cat','dog']
a.extend(b)
print(a)
b.extend(a)
print(b)
print('removing element from list\n 1.remove()\n 2.pop()\n 3.clear()\n 4.del')
fruits=['apple','banana','orange','grape','melon','kiwi','mango','grape','papaya']
print('before remove:',fruits)      
fruits.remove('grape')
print('after remove:',fruits)
fruits.pop(2)
print('after pop:',fruits)
del fruits[1:4]
print('after del:',fruits)
fruits.clear()
print('after clear:',fruits)
# remove removes the first occurrence of the specified element from the list. If the element is not found, it raises a ValueError.
# pop removes and returns the element at the specified index. If no index is specified, it removes and returns the last element of the list. If the index is out of range, it raises an IndexError.
# clear removes all elements from the list, leaving it empty. The list itself still exists but contains no items.
#del is a keyword that can be used to delete an element at a specific index or a slice of elements from the list. It can also be used to delete the entire list. If you try to access an element that has been deleted, it will raise a NameError.