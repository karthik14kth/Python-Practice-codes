a=[]
#a=[6,-3,0,8,5]
def user_input_mylist(my_list): #Get user input to generate a random list
    import random,sys
    Range=input(("Enter the range as positive integer"))
    lower=input("Enter the lower limit")
    upper=input("Enter the upper limit:")
    if int(upper)>int(lower):
        for i in range(int(Range)):
            my_list.append(random.randint(int(lower),int(upper)))
            #print(a)
    else:
        print("one or more inputs are invalid")
        sys.exit()
    return my_list

a=user_input_mylist(a)
print("The original list is:", a)

def bubble_sort(a):

    for i in range(len(a)-1):
        if a[i] < a[i+1]:
            #print(f"No sorting iteration {i}")
            continue
        else:
            a[i],a[i+1]=a[i+1],a[i]
            #print(f"list after iteration {i} is {a}")
    if sorted(a)== a:
        return a
    else:
        bubble_sort(a)
        return(a)

print("The bubble sorted list is",bubble_sort(a))
