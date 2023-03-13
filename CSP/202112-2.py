n, N = map(int, input().split())
a = list(map(int, input().split()))
a.insert(0, 0)
ans = 0
r = N // (n + 1)

for i in range(1, n):
    f = a[i - 1]
    g = i // r
    ans += abs(f - g)

