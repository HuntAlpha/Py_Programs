n=int(input())
p=n
l=[]
k=n
for i in range(p,2,-1):
    c=0
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c==0 and i!=n:
        l+=[i]
        break
while True:
    n+=1
    c1=0
    for i in range(2,n):
        if n%i==0:
            c1=c1+1
    if c1==0 and n!=k:
        l+=[n]
        break
print(min(l))