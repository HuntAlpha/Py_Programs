n=input()
s=0
p=1
for i in range(len(n)):
    s+=int(n[i])
    p*=int(n[i])
if s==p:
    print("Spy Number")
else:
    print("No")