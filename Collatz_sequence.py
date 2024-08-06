number=int(input("Enter a positive integer:"))
print("The number considered is",number)
if number%2==0:
    print("Number is even")
else:
    print("Number is odd")
def even_odd_collatz(number):
    while number!=1:
        yield (number)
        if number%2==0:
            number=number//2
        else:
            number=3*number+1

    yield 1

sequence =even_odd_collatz(number)

for j in sequence:
    print(j,end=' ')






