n=int(input())
a=list(map(int,input().split()))
c=[]
for i in range(n):
    if (a[i]==i):
        c.append(str(a[i]))
c.sort()
if(len(c)==0):
    print("-1")
else:
    print(" ".join(c))
