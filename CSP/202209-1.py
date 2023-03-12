import itertools
from itertools import accumulate
import operator
from operator import mul

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(accumulate(a, operator.mul))
c.insert(0, 1)
b = []
res = 0
for i in range(len(c) - 1):
    b_i = (m % c[i + 1] - res) / c[i]
    res = m % c[i + 1]
    print(int(b_i), end = ' ')
    b.append(b_i)

