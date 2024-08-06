def fibonacci(num):
    m=0
    n=1
    print(m,n,end=' ')
    for i in range(1, num - 1):
        x = m + n
        yield x
        m = n
        n = x


s = int(input("enter the fibonacci series length greater than 1: "))
a = fibonacci(s)

print(f"The fibonacci  series length of {s} are given below:")

for i in a:
    print(i,end= ' ')
    i+=1