n = int(input())
ans = 0
for i in range(n):
    w, score = map(int, input().split())
    ans += w * score

print(max(0, ans))