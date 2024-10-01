a=int(input())
b=int(input())
for i in range(a,b+1):
    x=str(i)
    s=0
    p=1
    for j in range(len(x)):
        s+=int(x[j])
        p*=int(x[j])
    if s==p:
        print(x,end=' ')