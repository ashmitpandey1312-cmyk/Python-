print("Test grading range")
a=int(input("Enter marks for Maths"))
b=int(input("Enter marks for chemistry"))
c=int(input("Enter marks for physics"))
d=int(input("Enter marks for English"))
e=int(input("Enter marks for Biology"))
Percentage=a+b+c+d+e/100 *100
print("Percentage=",Percentage)
if Percentage>=90:
    print("A")
elif Percentage<=89 and Percentage>=75:
    print("B")
elif Percentage<=74 and Percentage>=60:
    print("C")
elif Percentage<=59 and Percentage>=40:
    print("D")
else:
    print("fail")
    
            
