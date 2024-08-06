def power_till_exponent(num,exp):
    from math import pow
    for i in range(1,exp+1):
        yield int(pow(num,i))

power_number= int(input("Enter the number needed:"))
exponent=int(input("Enter the exponent for power calculation:"))
answer = power_till_exponent(power_number,exponent)  #generator object starts

for j in answer:
    print(j)