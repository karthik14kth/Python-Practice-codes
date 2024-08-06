def numbers(i):
    from math import pow
    for i in range(1, i+1):
        yield pow(i,(1/3)), pow(i,(1/2))

s = int(input("enter the number greater than 1: "))
a = numbers(s)

i = 1
print(f"The cube root & square root upto {s} are given in the form of tuples below:")
while i <= s:
    print(next(a))
    i+=1