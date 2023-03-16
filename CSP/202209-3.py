import collections
from collections import defaultdict
n = int(input())
risk_dis = {} # 存储每个地区开始计算风险区的日子

for date in range(n):
    ans = set({})
    risk_list = list(map(int, input().split()))
    l, m = risk_list[0], risk_list[1]
    risk_list.pop(0)
    risk_list.pop(1)
    for i in range(l): # 更新风险区名单
        if r[i] in risk_dis:
            risk_dis[risk_list[i]] = max(date, risk_dis[risk_list[i]]) # 如果之前是风险区 那就更新
        else:
            risk_dis[risk_list[i]] = date

    m = r[1]
    for j in range(m):
        d, u, r = map(int, input().split())
        if r in risk_dis and risk_dis[r[i]] <= d < risk_dis[r[i]] + 7 and risk_dis[r[i]] + 6 >= date: # 用户到的地方在风险区名单里，且到达日期是风险时间
            ans.add(u)
    ans = list(ans)
    ans.sort()
    print(date, end = ' ')
    for a in ans:
        print(a, end = ' ')
    print('')
    

        