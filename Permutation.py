a=[]
def user_input_mylist(a):
    import random
    Range=input(("Enter the range"))
    lower=input("Enter the lower limit")
    upper=input("Enter the upper limit:")
    if int(upper)>int(lower):
        for i in range(int(Range)):
            a.append(random.randint(int(lower),int(upper)))
    else:
        a="one or more inputs are invalid"
    return a

a=user_input_mylist(a)
print("The original list is:", a)

def all_permutations(my_list):
    from itertools import  permutations  #Gives all permutaions
    yield (list(permutations(my_list)))

all_permutations_gen=all_permutations(a)
print("The possible list permutations are:")
for j in  all_permutations_gen:
    print(j)