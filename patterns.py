# pattern1
# for i in range(5):
#    print("*****")
# print()
# pattern2
# for i in range(5, 0, -1):
#     print("*" * i)
# print()
#pattern3
# rows=5
# for i in range(1, rows + 1):
#     spaces = ' ' * (rows - i)
#     print(spaces + "*" * i)
# pattern4
# rows=5
# for i in range(rows, 0, -1):
#     spaces = ' ' * (rows - i)
#     print(spaces + "*" * i)
# pattern5
# rows = 3
# for i in range(1, rows + 1):
#     for j in range(1, rows * 2):
#         if j == rows - i + 1 or j == rows + i - 1:
#             print("*", end="")
#         elif i == rows and j % 2 != 0:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# pattern6
# n = 5
# for i in range(1, n + 1):
#     print(' ' * (n - i) + '*' * i)
# for i in range(n - 1, 0, -1):
#     print(' ' * (n - i) + '*' * i)
# pattern7
# rows = 3
# for i in range(1, rows + 1):
#     print(' ' * (rows - i) + '*' * (2 * i - 1))
# pattern8
# n = 4
# num = 1
# for i in range(1, n + 1):
#     for j in range(i):
#         print(num, end=" ")
#         num += 1
#     print()
# pattern9
# n = 4
# num = 10
# for i in range(1, n + 1):
#     for j in range(i):
#         print(num, end=" ")
#         num -= 1
#     print()
# # pattern10
# n = 10
# for i in range(1, n + 1):
#     for j in range(i):
#         print((i + j) % 2, end="")
#     print()
# # pattern11
# n = 4
# for i in range(1, n + 1):
#     print(" " * (n - i), end="") 
#     for j in range(1, i + 1):
#         print(j, end="")
#     for j in range(i - 1, 0, -1):
#         print(j, end="")
    # print()
# # pattern12
# n = 3
# for i in range(n):
#     print(" " * (n - i - 1), end="")
#     for j in range(i, -1, -1):
#         print(j, end="")
#     for j in range(1, i + 1):
#         print(j, end="")
#     print()
# # pattern13
# n = 4
# for i in range(1, n + 1):
#     print(" " * (n - i), end="")
#     for j in range(1, 2 * i):
#         print(j, end="")
#     print()
# # pattern14
# n = 4
# for i in range(1, n + 1):
#     for j in range(i):
#         print((i + j + 1) % 2, end="")
#     print()
# # pattern15
# for i in range(1, 6):
#     print(i, i + 1)
# # pattern16
# n = 4
# for i in range(n):
#     print(str(i) * (i + 1))

m=8
for i in range(m):
    print(str(i) * (i + 1))
o=7
for i in range(o):
    print(str(i) * (i + 1))
# if you want toprint khwopa  then kh ,kho,khwo,khwop,khwopa
k="khwopa"
for i in range(2, len(k) + 1):
    print(k[:i])
#pattern17
n = 5
for i in range(1, n + 1):
    print(str(i) * i)
    # pattern18
n = 5
for i in range(1, n + 1):
    print(str(i) * (n - i + 1))
# loop under loop
l=5
for i in range(1, l + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
    # pattern19
n = 5
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j, end="")
    print()