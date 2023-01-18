#write a program to find maximum between three numbers.
a=int(input('Enter No1'))
b=int(input('Enter No2'))
c=int(input('Enter No3'))
max = (a if (a > b and a > c) else
 (b if (b > a and b > c) else c))
print('maximum number is',max)