n=int(input('enter n value='))
k=5
for i in range(1,n+1):
    for j in range(1,i+1):
        if(i==1):
            print(i,end=' ')
        else:
            print(k,end=' ')
            k=k+5
    print()