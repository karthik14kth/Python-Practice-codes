def primeNo(num1,num2):
    for i in range(num1,num2+1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            yield i

s1 = int(input("enter the number greater than 1: "))
s2 = int(input("enter the number greater than 1: "))
a = primeNo(s1,s2)

print(f"The primes upto {s2} from {s1} are given below:")

for i in a:
    print(i,end=' ')
    i+=1