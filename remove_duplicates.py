l=list(map(int,input().split()))
r=[]
for i in l:
    if i not in r:
        r.append(i)
r.sort()
print("Before:",l)
print("After: ",r)