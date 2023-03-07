n, k = map(int, input().split())
p = list(map(float, input().split()))

dp = []
for i in range(105):
    dp.append([0.0] *(1 << 17))
# print(len(dp[0]), len(dp))
cnt = [0] * (1 << n)
for i in range(len(cnt)): # 预处理 x中1的个数就是当前有几种手牌
    x = i
    while x:
        x &= x - 1
        cnt[i] += 1

ans = 0.0
dp[0][0] = 1
for s in range(1 << n):
    for i in range(85):
        if cnt[s] + (i - cnt[s]) // k == n:
            ans += i * dp[i][s] # 满足终止条件 不用接着抽了
            continue

        for j in range(1, n): # 枚举每种抽到的卡牌
            if s & (1 << j): #又抽到了重复的
                dp[i + 1][s] += dp[i][s] * p[j]
                # print(i + 1, s, dp[i + 1][s], dp[i][s], p[j])    
            else:
                dp[i + 1][s + (1 << j)] += dp[i][s] * p[j] # 新状态s + (1 << j)
            # print(i, s, dp[i][s], p[j])

print('%.10f'%ans)


    