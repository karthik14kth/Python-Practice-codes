number=int(input("Enter a number"))

def factor(num):
    for i in range(2,num+1):
            if num%i==0:
                for j in range(2,i):
                    if i%j==0:
                        break
                else:
                    yield i

print("The prime factors aprt from 1 are:")
a=factor(number)

for j in a:
    print(j,end=' ')

