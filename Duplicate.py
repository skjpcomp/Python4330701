n=int(input('How many elements required for list'))
lst=[]
for i in range(1,n+1):
     lst.append(int(input('Enter Element')))
print('original list:',lst)
c=[]
for i in lst:
     if i not in c:
         c.append(i)
print('After removing duplicatevalue:',c)