n=int(input())
m=int(input())
c=0
l=[]
for i in range(n,m+1):
    s=0
    k=str(i)
    for j in range(len(k)):
        s+=int(k[j])**len(k)
    if s==i:
        c+=1
        l.append(i)
print(c)
for i in l:
    print(i,end=' ')