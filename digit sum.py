print("print the sum of 3 digits")
s=int(input("Enter the 3 digits"))
Last=s%10
s=s//10
middle=s%10
s=s//10
first=s%10
Num=Last+middle+first
print("The sum of 3 digits are ", Num)
