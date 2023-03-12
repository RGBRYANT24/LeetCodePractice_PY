n, x = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

stk = [(2 ** n - 1, sum(a))]
ans = sum(a)
vis = set({})
vis.add(2 ** n - 1)
while len(stk):
    s, cost = stk.pop(0)
    for i in range(n):
        # print(i, 1 << i, s)
        new_s = s ^ (1 << i)
        if new_s not in vis and s & (1 << i) != 0 and cost - a[i] >= x:
            ans = min(ans, cost - a[i])
            stk.append((new_s, cost - a[i]))
            vis.add(new_s)
print(ans, end = '')
