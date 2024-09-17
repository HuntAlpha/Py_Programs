n=int(input())
c=0
if n<=0:
    print("Invalid Number")
else:
    if n==1:
        print("Not Prime")
    else:
        for i in range(2,n//2+1):
            if n%i==0:
                c+=1
        if c==0:
            print("Prime")
        else:
            print("Not Prime")