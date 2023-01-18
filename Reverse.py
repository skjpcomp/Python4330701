no=int(input("Enter no:"))
temp=no
rev=0
while(no>0):
    no1=no%10
    rev=rev*10+no1
    no=int(no/10)

print("Original no:",temp)
print("Reverse no:",rev)