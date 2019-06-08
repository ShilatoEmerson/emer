k=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
for i in range(k):
  print(l[i],end="")
