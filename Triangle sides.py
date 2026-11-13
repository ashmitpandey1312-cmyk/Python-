print("write a program to accept three sides of a triangle and check if it is a equilateral,isosceles and scalene triangle")
a=int(input("Enter the side"))
b=int(input("Enter the side"))
c=int(input("Enter the side"))

if a==b and b==c and a==c:
    print("The triangle is equilateral Triangle")
elif a==b and b==a:
    print("The triangle is isosceles Triangle")
else:
    print("It is a scalene triang;e")
    
