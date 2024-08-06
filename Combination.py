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


def all_combinations(my_list,list_length):
    from itertools import combinations  #Gives all permutaions
    yield (list(combinations(my_list,list_length)))

for i in range(1,len(a)+1):
    combination_posiblities=all_combinations(a,i)
    print(f'The combinations of {len(a)}C{i}:')
    for j in combination_posiblities:
        print(j)

