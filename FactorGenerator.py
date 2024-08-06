number=int(input("Enter a number"))

def factor(num):
    for i in range(2,num+1):
            if num%i==0:
                yield i



print("The factors apart from 1 are:")
a=factor(number)

for j in a:
    print(j,end=' ')

