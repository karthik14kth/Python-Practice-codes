a = 33320
i = 0
j= 0
salary = [ ]
while (i <= 35):
   x =  pow(1.03,int(i))
   y = int(x * a * 12)
   #print (y)
   salary.append(y)
   i +=1
#print("The list is \n",salary)
#######print(len(salary))
print("The total sum you should have is SEK",sum(salary))




''' 
p = 0
j=1
while (j <= 10):
   p = p+j
   j +=1
print (p)
'''