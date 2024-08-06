
def my_int(a):
    my_set=set()
    while True:
        if a == 1:
            return True
        elif a in my_set:
            return False
        my_set.add(a)
        a=sum(int(i)**2 for i in str(a))

#Referred author's code

num= int(input(("Enter a Number")))

def happy_check(num):
    while True:
        num+=1
        b=my_int(num)
        if b== True:
            yield num

y=happy_check(num)
print(next(y))












































































