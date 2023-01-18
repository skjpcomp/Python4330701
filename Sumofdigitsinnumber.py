no=int(input("Enter no:"))
temp=no
sum=0
while(no>0):
    no1=no%10
    sum=sum+no1
    no=int(no/10)

print("Original no:",temp)
print("Sum of digit no:",sum)