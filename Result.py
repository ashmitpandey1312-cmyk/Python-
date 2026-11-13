print("Write a program to accept three subjects and calculate and display total marks,percentage and grade obtained based on the following table")
a=int(input("Enter the marks for Maths"))
b=int(input("Enter the marks for chemistry"))
c=int(input("Enter the marks for physics"))
totalmarks=a+b+c
print("Total marks is",totalmarks)
percentage=totalmarks/300*100
print("Percentage is",percentage)

if percentage>90:
            print("The grade obtained is A+")
elif percentage<90 and percentage>80:
            print("The grade obtained is A")
elif percentage<80 and percentage>65:
            print("The grade obtained is B+")
elif percentage<65 and percentage>50:
            print("The grade obtained is B")
elif percentage<50 and percentage>40:
            print("The grade obtained is c+")
else:
    print("You have failed")
    
            
