n, N = map(int, input().split())
a = list(map(int, input().split()))


ans = 0
a.insert(0, 0)
for i in range(1, len(a)):
    ans += (a[i] - a[i - 1]) * (i - 1)

ans += (N - a[-1]) * n
print(ans)