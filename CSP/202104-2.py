n, L, r, t = map(int, input().split())
g = []
for i in range(n):
    g.append(list(map(int, input().split())))

def check(x, y):
    res = count = 0
    # print(x, y, max(0, x - r), min(n, x + r), max(0, y - r), min(n, y + r))
    for i in range(max(0, x - r), min(n, x + r + 1)):
        for j in range(max(0, y - r), min(n, y + r + 1)):
            res += g[i][j]
            # print(i, j, end = ' ')
            count += 1
        # print('')
    # print(x, y, res / count, res / count <= t)
    return True if res / count <= t else False

ans = 0
for i in range(n):
    for j in range(n):
        if check(i, j):
            ans += 1

print(ans)