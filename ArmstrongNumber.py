def Armstrong_number(num):
    while True:
        armstrong = sum(int(num_cube)**len(str(num)) for num_cube in str(num))
        if num== armstrong:
            return True
        return False


def armstrong_check(num):
    while True:
        num+=1
        b=Armstrong_number(num)
        #print(b)
        if b== True:
            yield num

num= int(input(("Enter a Number:")))

y=armstrong_check(num)
print("Next armstrong number is",next(y))


