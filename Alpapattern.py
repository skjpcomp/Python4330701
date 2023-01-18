n=int(input('enter n value='))
num=65
for i in range(1,n+1):
    for j in range(1,i+1):
        ch=chr(num)
        print(ch,end=' ')
        num=num+1
    print()
    