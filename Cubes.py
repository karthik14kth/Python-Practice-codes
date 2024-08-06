def numbers(i):
    for i in range(1, i+1):
        yield i ** 3

s = int(input("enter the number greater than 1: "))
a = numbers(s)

i = 1
print(f"The cubes upto {s} are given below:")
while i <= s:
    print(next(a))
    i+=1