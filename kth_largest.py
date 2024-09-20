l=list(map(int,input("Enter values: ").split()))
k=int(input("Enter kth value: "))
r=[]
for i in l:
    if i not in r:
        r.append(i)
r.sort()
print(r)
print("kth Largest: ",r[-(k)])