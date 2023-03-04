import functools
from collections import defaultdict
def cmp(a,b):
    A = a[-1]
    B = b[-1]
    if A != B:
        return ord(B) - ord(A)
    else:
        if A == 'L':
            return len(a) - len(b)
        else:
            return len(b) - len(a)
n = int(input())
p = input().split()
m = int(input())
q = input().split()
st = set()
for x in p:
    st.add(x)
for x in q:
    st.add(x)
arr = list(st)
arr.sort(key=functools.cmp_to_key(cmp))
mp = defaultdict(int)
index = 1
for x in arr:
    mp[x] = index
    index += 1
vis = [0] * n
pp = []
qq = []
for x in p:
    pp.append(mp[x])
for x in q:
    qq.append(mp[x])
pp.sort()
qq.sort()
lc = 0
ff = 0
for i in range(m):
    now = qq[i]
    while lc < n and pp[lc] < now:
        lc += 1
    if lc < n:
        lc += 1
    else:
        ff = 1
if ff == 1:
    print("No")
else:
    print("Yes")