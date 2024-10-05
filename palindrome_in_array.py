l=list(input().split())
p=[]
q=[]
for i in l:
    if i==i[::-1]:
        p.append(i)
    else:
        q.append(i)
print(p,q)