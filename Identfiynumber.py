n=int(input('How many elements required for list'))
lst=[]
for i in range(1,n+1):
     lst.append(int(input('Enter Element')))
print(lst)
pos=0
neg=0
zer=0
odd=0
even=0
sum1=0
for i in lst:
    sum1=sum1+i
    avg=sum1/n
if i% 2==0:
    even+=1
else:
    odd+=1
if i>0:
    pos+=1
elif i<0:
     neg+=1
else:
    zer+=1
print('total even numbers are:',even)
print('total odd numbers are:',odd)
print('total positive numbers are:',pos)
print('total negative numbers are:',neg)
print('total zero numbers are:',zer)
print('Average of all numbers are:',avg)
