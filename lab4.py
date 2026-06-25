# #1.WAP to print all the items in a list
# list=['Ram','Sita','Hari','Gita']
# for item in list:
#     print(item)
# print()
# #2WAP to print all the veven numbers from 1 to 10
# for i in range(1,11):
#     if i%2==0:
#         print(i,end=" ")
# print()
# #3WAp to get the largest and smallest number in a list without using built in the function
# list1 = [99, 0, 1, 5, 87, 54, 9]

# smallest = largest = list1[0]

# for num in list1:
#     if num < smallest:
#         smallest = num
#     if num > largest:
#         largest = num

# print("Smallest number =", smallest)
# print("Largest number =", largest)

# #4WAP to find the second smallest and second largest numbers in a list.
# list2=[99,0,1,5,87,54,9]
# list2.sort()
# print("The second largest number is:",list2[-2])
# print("The second smallest number is:",list2[1])
# print()


# #5WAP to sum all items in a list
# list2=[3,6,9,56]
# sum=0
# for i in list2:
#     sum+=i
# print("The sum of the numbers in a list is:",sum,"\n")

# #6WAp to multiply all the items in a list
# list3=[3,8,9,6]
# mul=1
# for i in list3:
#     mul*=i
# print("The multiplication of the numbers in a list is:",mul,"\n")
# #7WAP to check whether a list is empty or not
# list4=['Ram','Hari','Gita']
# if len(list4)==0:
#     print("List is empty\n")
# else:
#     print("List is not empty\n")
# #8WAP to print the numbers of a specified list after removing even number from it
# list5=[45,76,88,12,18,55,121,131,44,66,99,55,100,98]
# result=[]
# for i in  list5:
#     if i %2 != 0:
#         result.append(i)
# print("The result after removing even numbers in a list:",result,"\n")
# #9WAP to print a specified list after removing 0th,4th and 5th element
# list_sample=['Red','Green','White','Black','Pink','Yellow']
# result=[list_sample[i] for i in range(len(list_sample)) if i not in[0,4,5]]
# print(result)
# # list_sample.pop(0)
# # list_sample.pop(4)
# # list_sample.pop()
# # print(list_sample)
# # 10 WAP check if each number is prime in a given list of numbers.print prime numbers if any else print no prime numbers
# list8=[3,2,1,5,7,98,67,45,33,29,94,121,71]
# primenumbers=[]
# for num in list8:
#     if num>1:
#      is_prime=True
#      for i in range(2,num):
#       if num%i==0:
#         is_prime=False
#         break
#      if is_prime:
#         primenumbers.append(num)
# if primenumbers:
#    print(primenumbers)
# else:
#    print("No Prime Numbers")
#11WAP to remove duplicates in a list
# list9=[4,5,7,9,22,1,7,4,9]
# print('The list before:',list9)
# result=list(set(list9))
# print("The result is: ",result,'\n')
#12WAP to merge two lists and remove duplicates from the combined list
# list1=[9,6,7,0,3,4,6]
# list2=[8,7,0,3,2,1,88]
# print("The list1 contains:",list1)
# print("The list2 contains:",list2)
# result=list(set(list1+list2))
# print("The result is:",result)
# # # 13WAP to print a list in reverse order
# list2=[8,7,0,3,2,1,88]
# print('List before reverse:',list2)
# print('List after reverse:',list2[::-1])
# #14WAP to sort given list of strings(numbers) numerically
# list=['4','7','8','0','5']
# print("List before:",list)
# list.sort(key=int)
# print('List after:',list)
# # # 15Apply different functions like append,remove,pop,insert,sort,max,min in a list
# list=[5,7,88,23,11,56,77,60,455,231]
# print('Initial List:',list)
# list.append(100)
# print('List after appending 100:',list)
# list.remove(88)
# print('List after removing 88:',list)
# list.pop()
# print('List after pop:',list)
# list.insert(1,18)
# print('List after insert:',list)
# list.sort()
# print('List after sort:',list)
# print('Max number:',max(list))
# print('Min number:',min(list))
# print()
# #16 WAPn to copy content of one list to another
# list9=['cat','dog','rabbit','panda']
# print("The initial lis",list9)
# new_list=list9.copy()
# print('The list after being copied is:',new_list)
# print()
# # # 17WAP to sort a list of lists by a given index of inner list
# list=[[2,5],[1,8],[4,3]]
# print('The list before is:',list)
# list.sort(key=lambda x:x[1])
# print(list)
# # 18WAP to generate and print a list of the first and last 5 elements where the values are square numbers between 1 and 15(both included)
# square=[x*x for x in range(1,16)]
# print("First 5:",square[:5])
# print("Last 5:",square[-5:])
# # 19WAP to insert a given string at the beginning of all items in a list
# list_sample=[1,2,3,4]
# string='emp'
# result=[string+str(i) for i in list_sample]
# print(result)
# # 20 WAP to insert n values in a list and find those values in a list that are greater than a specified number
# n=int(input("Enter number of elements"))
# list=[]
# for i in range(n):
#     list.append(int(input('Enter a value:')))
# limit=int(input('Enter comparison number:'))
# for num in list:
#     if num>limit:
#         print(num)
# a,b=3.3,3
# c=a//b
# print(c)
# m,n=12,5
# print(m//n)
# m1,n1=-12,5
# print(m1//n1)