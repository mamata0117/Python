# 1. Write a Python program to create a list of five student names and print the list.

students = ["Ram", "Sita", "Hari", "Gita", "Krishna"]

print("List of students:", students)


# 2. Write a Python program to access and print the first, last, and middle elements of a list.

students = ["Ram", "Sita", "Hari", "Gita", "Krishna"]

print("First element:", students[0])
print("Middle element:", students[2])
print("Last element:", students[-1])


# 3. Write a Python program to perform list concatenation and repetition operations.

list1 = [1, 2, 3]
list2 = [4, 5, 6]

print("Concatenated List:", list1 + list2)
print("Repeated List:", list1 * 2)


# 4. Write a Python program to change the value of a specific element in a list.

students = ["Ram", "Sita", "Hari", "Gita", "Krishna"]

students[1] = "Rita"

print("Updated List:", students)


# 5. Write a Python program to add elements to a list using append() and insert() methods.

students = ["Ram", "Sita", "Hari"]

students.append("Gita")
students.insert(1, "Krishna")

print("Updated List:", students)


# 6. Write a Python program to remove elements from a list using remove(), pop(), and del.

students = ["Ram", "Sita", "Hari", "Gita"]

students.remove("Hari")
students.pop()
del students[0]

print("Updated List:", students)


# 7. Write a Python program to sort a list permanently using the sort() method.

numbers = [5, 2, 8, 1, 9]

numbers.sort()

print("Sorted List:", numbers)


# 8. Write a Python program to sort a list temporarily using the sorted() function.

numbers = [7, 3, 6, 2]

print("Temporary Sorted List:", sorted(numbers))
print("Original List:", numbers)


# 9. Write a Python program to print a list in reverse order using the reverse() method.

numbers = [1, 2, 3, 4, 5]

numbers.reverse()

print("Reversed List:", numbers)


# 10. Write a Python program to find the length of a list using the len() function.

students = ["Ram", "Sita", "Hari", "Gita"]

print("Length of list:", len(students))


# 11. Write a Python program to demonstrate index error handling while accessing list elements.

students = ["Ram", "Sita", "Hari"]

try:
    print(students[5])

except IndexError:
    print("Index out of range")


# 12. Write a Python program to create a numerical list using the range() function.

numbers = list(range(1, 11))

print(numbers)


# 13. Write a Python program to generate a list of even numbers from 1 to 50 using range().

even_numbers = list(range(2, 51, 2))

print(even_numbers)


# 14. Write a Python program to print all elements of a list using a loop.

students = ["Ram", "Sita", "Hari", "Gita"]

for name in students:
    print(name)


# 15. Write a Python program to print only the first three elements of a list using slicing.

students = ["Ram", "Sita", "Hari", "Gita", "Krishna"]

print(students[:3])


# 16. Write a Python program to extract and print a slice of a list from index 2 to index 5.

numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers[2:6])


# 17. Write a Python program to loop through a sliced portion of a list.

numbers = [10, 20, 30, 40, 50, 60]

for item in numbers[1:4]:
    print(item)


# 18. Write a Python program to create a copy of a list and demonstrate that modifying one list does not affect the other.

list1 = ["Ram", "Sita", "Hari"]

list2 = list1[:]

list2.append("Gita")

print("Original List:", list1)
print("Copied List:", list2)


# 19. Write a Python program to find the maximum and minimum values in a numerical list.

numbers = [12, 45, 7, 89, 23]

print("Maximum Value:", max(numbers))
print("Minimum Value:", min(numbers))


# 20. Write a Python program to count how many times a specific element appears in a list.

numbers = [1, 2, 3, 2, 2, 4]

print("Count of 2:", numbers.count(2))


# 21. Write a Python program to define a tuple containing five colors and print all elements.

colors = ("Red", "Blue", "Green", "Yellow", "White")

print(colors)


# 22. Write a Python program to access individual elements of a tuple using indexing.

colors = ("Red", "Blue", "Green", "Yellow", "White")

print(colors[0])
print(colors[2])
print(colors[-1])


# 23. Write a Python program to loop through all values in a tuple using a for loop.

colors = ("Red", "Blue", "Green", "Yellow", "White")

for color in colors:
    print(color)


# 24. Write a Python program to demonstrate tuple immutability by attempting to modify a tuple element.

colors = ("Red", "Blue", "Green")

try:
    colors[1] = "Black"

except TypeError:
    print("Tuple elements cannot be changed")


# 25. Write a Python program to create a new tuple by rewriting an existing tuple with additional elements.

colors = ("Red", "Blue", "Green")

new_colors = colors + ("Black", "Pink")

print(new_colors)