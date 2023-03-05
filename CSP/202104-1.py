import collections
from collections import defaultdict

n, m, L = map(int, input().split())
grid = []
for i in range(n):
    temp = list(map(int, input().split()))
    grid.append(temp)

ans = [0] * L
for i in range(n):
    for j in range(m):
        ans[grid[i][j]] += 1

s = ' '.join('%s' %num for num in ans)
print(s)
