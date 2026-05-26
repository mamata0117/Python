units=float(input("Enter the number of units consumed: "))
# if units <= 100:
#     bill = units * 0.5
# elif units <= 200:
#     bill = 100 * 0.5 + (units - 100) * 0.75
# elif units <= 300:
#     bill = 100 * 0.5 + 100 * 0.75 + (units - 200) * 1.20
# else:
#     bill = 100 * 0.5 + 100 * 0.75 + 100 * 1.20 + (units - 300) * 1.50
# print(f"Your electricity bill is: {bill:.2f}\n")
# #18menu driven system using python match case  area of circle,rectangle and triangle
# operation=int(input("Enter the shape you want to calculate area for \n 1.Circle \n 2.Rectangle \n 3.Triangle \n"))
# match operation:
#     case 1:
#         radius=float(input("Enter the radius of the circle: "))
#         area=3.14159*radius**2
#         print(f"The area of the circle is: {area:.2f}")
#     case 2:
#         length=float(input("Enter the length of the rectangle: "))
#         width=float(input("Enter the width of the rectangle: "))
#         area=length*width
#         print(f"The area of the rectangle is: {area:.2f}")
#     case 3:
#         base=float(input("Enter the base of the triangle: "))
#         height=float(input("Enter the height of the triangle: "))
#         area=0.5*base*height
#         print(f"The area of the triangle is: {area:.2f}")
#     case _:
#         print("Invalid option.\n")
# print("\n")  
# #19 use match case to display the day name based on day number entered by user
# daynum=int(input("Enter a day number 1-7: "))
# match daynum:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("Invalid day number.")