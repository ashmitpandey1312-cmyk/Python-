print("whether it is a leap year or not")
s=int(input("Enter your leap year"))
if(s%4==0 and s%100 !=0) or (s%400==0):
    print("It is a leap year")
else:
    print("It is not a leap year")
    
    
