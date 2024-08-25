# ------------------area calculator-------------

print("******************area calculator************")
print("""press 1 to get the area of square 
 press 2 to get the area of rectangle
 press 1 to get the area of circle
press 1 to get the area of triangle""")

choice = int(input("enter number between 1-4:"))

if choice == 1:
    side = float(input("enter length of one side: "))
area = side ** 2
print("the area of square is", area)
elif choice == 2
length = float(input("enter length of rectangle: "))
width = float(input("enter width of rectangle: "))
area = length * width
print("the area of rectangle is", area)

elif choice == 3:
radius = float(input("enter radius of circle: ")) \
    area = ((22 / 7) * (radius ** 2))
print("the area of circle is", area)

elif choice == 4:
base = float(input("enter base of triangle:"))
height = float(input("enter height of triangle:"))
area = 0.5 * base * height
print("the area of triangle is", area)
else:
print("invalid input")
