n, L, r, t = map(int, input().split())
g = []
g.append([0] * (n+ 2))
for i in range(n):
    temp = list(map(int, input().split()))
    temp.insert(0, 0)
    temp.append(0)
    g.append(temp)
g.append([0] * (n + 2))
# print(g)
a = [[0] * (n + 2) for _ in range(n + 2)]
# print(len(a), len(a[0]), a)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        # print(i, j, g[i - 1][j], g[i][j - 1], g[i - 1][j - 1])
        a[i][j] = a[i - 1][j] + a[i][j - 1] - a[i - 1][j - 1] + g[i][j]

# print(a)
def check(x, y):
    down_x = min(n, x + r)
    down_y = min(n, y + r)
    up_x = max(1, x - r)
    up_y = max(1, y - r)
    res = a[down_x][down_y] - a[down_x][up_y - 1] - a[up_x - 1][down_y] + a[up_x - 1][up_y - 1]
    count = (down_x - up_x + 1) * (down_y - up_y + 1)
    # print(x, y, down_x, down_y, up_x, up_y, res, count)
    return True if res / count <= t else False

ans = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if check(i, j):
            ans += 1

print(ans)