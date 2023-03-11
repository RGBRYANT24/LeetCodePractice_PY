import math

n = int(input())
a = list(map(int, input().split()))
mean = sum(a) / n
var = 0
for i in range(n):
    var += (a[i] - mean) ** 2
var /= n
var = math.sqrt(var)

for i in range(n):
    ans = (a[i] - mean) / var
    print('%.18f'%ans, end = ' ')

