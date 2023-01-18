no=int(input("Enter no:"))
temp=no
sum=0
while(no>0):
    no1=no%10
    sum=sum+no1*no1*no1
    no=int(no/10)
if(sum==temp):
    print("No is armstrong")
else:
    print("No is not armstrong")