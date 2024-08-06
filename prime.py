def primeNo(num):
    for i in range(1,num+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i

s = int(input("enter the number greater than 1: "))
a = primeNo(s)

print(f"The primes upto {s} are given below:")

for i in a:
    print(i)
    i+=1