l=list(map(int,input().split()))
r=[]
p=[]
for i in range(len(l)):
    if i%2==0:
        r.append(l[i])
        r.sort()
    else:
        p.append(l[i])
        p.sort()
p.reverse()
r.extend(p)
print(*r)