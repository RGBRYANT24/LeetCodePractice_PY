'''import collections
from collections import defaultdict

m = int(input())
l = []
d0 = defaultdict(int)
d1 = defaultdict(int)
for i in range(m):
    l.append(list(map(int, input().split())))
    if l[-1][1]:
        d1[l[-1][0]] +=1
    else:
        d0[l[-1][0]] += 1
a = [[0, 0]]
key = set(list(d1.keys()))
for k in d0.keys():
    key.add(k)
for k in key:
    a.append([a[-1][0] + d0[k], a[-1][1] + d1[k]])
print(a)
key = list(key)
ans = key[0]
count = -1
# a.pop(0)
for i in range(1, len(a)):
    if a[-1][1] - a[i - 1][1] + a[i - 1][0] >= count:
        ans = max(ans, key[i - 1])
        count = a[-1][1] - a[i - 1][1] + a[i - 1][0]

print(ans)'''           

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
l.sort()
sum = [0]
for i in range(n):
    sum.append(sum[-1] + l[i][1])

key = set({})
Max = res = 0
for i in range(n):
    k = l[i][0]
    if k in key:
        continue
    key.add(k)
    yuce1 = sum[n] - sum[i - 1]
    yuce0 = i - 1 - sum[i - 1]
    yuce = yuce1 + yuce0
    if yuce >= Max:
        Max = yuce
        res = k
print(res)