n ,X, Y = map(int, input().split())
dis = []
for i in range(n):
    x, y = map(int, input().split())
    dis.append([(X - x) ** 2 + (Y - y) ** 2,  i + 1])

dis.sort()
for i in range(3):
    print(dis[i][1])
