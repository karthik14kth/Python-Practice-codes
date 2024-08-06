
start = int(input("Enter starting number"))
end = int((input("Enter ending number")))
for i in range(start,end+1):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        print(i)








'''
for j in range(2,i+1,1):
    if i%j ==0:
        break

    prime = i
print(prime)

for i in range(start,end+1,1):
    print("number",i)
    for num in range(2,i//2):
        if num%2== 0:
            break
        else:
            print(i)
'''