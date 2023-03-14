import math
from math import pi
Q = []
for i in range(8):
    Q.append(list(map(int, input().split())))
n = int(input())
T = int(input())
a = list(map(int, input().split()))
M = [[0] * 10 for _ in range(10)]
i = j = k = 0
flag = [-1, 1] # 标志是左上还是右下 第一个是右下
while k < len(a):
    if (i == 0 or i == 7) and k < len(a): # 处理横着走
        # print(i, j)
        flag[0] *= -1
        flag[1] *= -1
        M[i][j] = a[k]
        j += 1        
        k += 1
        if k >= len(a):
            break
        # continue
    elif j == 0 or j == 7 and k < len(a):
        # print(i, j)
        flag[0] *= -1
        flag[1] *= -1
        M[i][j] = a[k]
        i += 1        
        k += 1
        if k >= len(a):
            break
        # continue
    if k >= len(a):
        break
    while (0 < i <= 7 or 0 < j <= 7) and k < len(a):
        # print(i, j)
        M[i][j] = a[k]
        # print(flag)
        i += flag[0]
        j += flag[1]
        k += 1
        if i == 0 or i == 7 or j == 0 or j == 7 or k >= len(a):
            break
    if k >= len(a):
        break

if T == 0:
    for i in range(8):
        for j in range(8):
            print(M[i][j], end = ' ')
        print('')

for i in range(8):
    for j in range(8):
        M[i][j] *= Q[i][j]

if T == 1:
    for i in range(8):
        for j in range(8):
            print(M[i][j], end = ' ')
        print('')

def A(x):
    return math.sqrt(0.5) if x == 0 else 1

new_M = [[0] * 10 for _ in range(10)]
for i in range(8):
    for j in range(8):
        res = 0
        for u in range(8):
            for v in range(8):
                temp = math.cos(pi * (float(i) + 0.5) * u / 8) * math.cos(pi * (float(j) + 0.5) * v / 8) * A(u) * A(v) * float(M[u][v])
                res += temp
                # print(temp)
        temp = int(res * 0.25 + 128 + 0.5)
        if temp > 255:
            temp = 255
        if temp < 0:
            temp = 0
        new_M[i][j] = temp
        # new_M[i][j] = res * 0.25

if T == 2:
    for i in range(8):
        for j in range(8):
            print(new_M[i][j], end = ' ')
        print('')


'''
16 11 10 16 24 40 51 61
12 12 14 19 26 58 60 55
14 13 16 24 40 57 69 56
14 17 22 29 51 87 80 62
18 22 37 56 68 109 103 77
24 35 55 64 81 104 113 92
49 64 78 87 103 121 120 101
72 92 95 98 112 100 103 99
26
0
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63
'''