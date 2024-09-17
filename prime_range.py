n=int(input())
m=int(input())
for i in range(n,m+1):
    c=0
    for j in range(2,i//2+1):
        if i%j==0:
            c=c+1
    if c==0 and i!=1:
        print(i,end=' ')