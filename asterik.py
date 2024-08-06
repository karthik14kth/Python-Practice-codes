number = int(input("Enter a number"))
n=""
for i in range(1,number+1,1):
    n += "*"
    print(n)
for j in range(number-1,0,-1):
    print(n[0:j])
