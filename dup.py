a=input()
b=input()
m= list(b)
s=[]
m.sort()
for i in range (len (m) -1):
  if m[i] == m[i+1] and m[i] not in s:
    s.append(m[i])
print (s)
