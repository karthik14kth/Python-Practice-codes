def numbers(i):
    import random
    for i in range(1, i+1):
        yield random.randint(1,i+1)

s = int(input("enter the number greater than 1: "))

num=numbers(s)
i=1
print("The generated random numbers are")
while i <= s:
    print(next(num))
    i=i+1