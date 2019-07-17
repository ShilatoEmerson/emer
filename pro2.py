from itertools import combinations
a,b=map(int,input().split())
c=len(str(a))
d=list(combinations(str(a),c-b))
d.sort()
print(''.join(d[0]))
