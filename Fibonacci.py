a = int(input("Enter range of numbers in integer"))
m= 0
n= 1
print("The fibonacci series for given range is")
print(m,end =' ')
print(n, end = ' ')
for i in range(1,a-1):
   x = m + n
   print(x,end = ' ')
   m =n
   n =x
