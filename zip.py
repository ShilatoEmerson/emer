a=int(input())
b=[]
for i in range(0,a):
    n=input()
    b.append(n)
c=[]
for i in zip(*b):
    if i.count(i[0])==len(i):
        c.append(i[0])
    else:
        break
print(''.join(c))
