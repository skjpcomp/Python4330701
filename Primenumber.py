no=int(input("enter no:"))
flag=0
for i in range(2,no):
    if(no%i==0):
        flag==1
        break
if(flag==0):
    print("Number is prime ")
else:
    print("Number is not prime ")