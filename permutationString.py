
a=input("Enter the string")
print("The original list is:", a)

def all_permutations(my_string):
    from itertools import  permutations  #Gives all permutaions
    yield (list(permutations(my_string)))

all_permutation_gen=all_permutations(a)

for j in  all_permutation_gen:
    #print(j,len(j))
    print(f"There would be {len(j)} combinations and they are:")
    for i in range (0,len(j)):
        print("".join(j[i]))