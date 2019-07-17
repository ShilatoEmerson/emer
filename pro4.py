a,b=map(str,input().split())
c=0
if len(a)>len(b):
    a,b=b,a
d=0
while d<len(a):
      c+=(ord(b[d])-ord(a[d]))
      d+=1
for d in range(d,len(b)):
      c+=ord(b[d])-ord('a')+1
print(c)
