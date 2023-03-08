import math
pow = math.pow

n, g = input().split()
out = list(map(float, input().split()))
n = int(n)
g = float(g)

res = 0
for i in range(len(out)):
    temp = out[i] * pow(1 + g, -i)
    res += temp

print('%.10f'%res)
