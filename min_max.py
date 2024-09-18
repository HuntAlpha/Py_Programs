l=list(map(int,input().split()))
p=0
q=l[0]
for i in range(len(l)):
    if l[i]>p:
        p=l[i]
    if l[i]<q:
        q=l[i]
print("Max: ",p)
print("Min: ",q)
