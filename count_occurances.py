l=list(map(int,input("Enter values: ").split()))
t=int(input("Enter Target value: "))
c=0
for i in range(len(l)):
    if l[i]==t:
        c+=1
print("Count: ",c)