number=input("enter the number")
s =" "
for i in range(len(number),0,-1):
    s+=number[int(i)-1]
print("The reversed number is:",int(s))
