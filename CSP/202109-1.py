import collections
from collections import defaultdict

a = defaultdict(int)

n = int(input())
b = list(map(int, input().split()))
max_num, min_num, max_ans, min_ans = 0, 0, 0, 0

for i in range(n):
	if max_num < b[i]:
		max_ans += b[i]
		max_num = b[i]
		min_ans += b[i]
	elif max_num >= b[i]:
		max_ans += max_num
		min_ans += min_num

for i in range(n):
	a[b[i]] += i
print(max_ans)
print(min_ans, end='')
	