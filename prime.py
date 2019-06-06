a,b=input().split()
c=0
for i in range(int(a),int(b)+1):
    x=1
    y=0
    while x<=i:
        if i%x==0:
            y+=1
        x+=1
    if y==2:
        c+=1
print(c)
