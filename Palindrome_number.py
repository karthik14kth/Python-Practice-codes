num=int(input("Enter the number:"))

def palindrome(no):
    while True:
        no+=1
        a=str(no)
        b = ' '
        for i in range(len(a) - 1, -1, -1):
            b += a[i]
        if no== int(b):
            yield no

a=palindrome(num)
print(next(a))