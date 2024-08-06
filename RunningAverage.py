def running_average():
    total=0
    count=0
    while True:
        if count >0:
            b= yield  total/count
        else:
            b= yield 0
        count+=1
        total+=b


average =running_average() #initialise generator object for its next instance
next(average)

while True:
    my_input=input("Enter the number for average(press 'e' to quit):")
    if my_input =='e':
        break
    my_number=float(my_input)

    my_average =average.send(my_number)
    print(my_average)

