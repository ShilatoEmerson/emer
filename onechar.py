w,x=input().split()
k=len(w)
m=len(x)
y=0
if k!=m:
    print("no")
else:
    for i in range(k):
        if  w[i]!=x[i]:
            y+=1
if y==1:
    print("yes")
else:
    print("no")
