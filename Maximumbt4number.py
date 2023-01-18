a=int(input("Enter value a:"))
b=int(input("Enter value b:"))
c=int(input("Enter value c:"))
d=int(input("Enter value d:"))
if (a>b and a>c and a>d):
    print(" a is maximum")
elif (b>a and b>c and b>d) :
    print("b is maximum")
elif (c>a and c>b and c>d) :
    print("c is maximum")
else:
    print("d is maximum")