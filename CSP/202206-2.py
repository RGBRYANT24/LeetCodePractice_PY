n, L, S = map(int, input().split())
m = []
for i in range(n):
    x, y = map(int, input().split())
    m.append((x, y))
m = set(m)
s = []
loc = []
for i in range(S+1):
    s.append(list(map(int, input().split())))

s.reverse()

for i in range(S + 1):
    for j in range(S + 1):
        if s[i][j] == 1:
            loc.append((i, j))
loc = set(loc)
ans = 0
for x, y in m:
    flag = True
    if x + S + 1 > L + 1 or y + S + 1 > L + 1:
        # print('oversize', x, y)
        continue
    for i, j in loc:
        if (x + i, y + j) not in m:
            flag = False
            break
    for i in range(S + 1):
        for j in range(S + 1):
            if (x + i, y + j) in m and s[i][j] != 1:
                flag = False
                # print('not fit', x + i, y + j)
                break
    if flag:
        # print(x, y)
        ans += 1
print(ans)
