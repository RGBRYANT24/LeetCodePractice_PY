#
# @lc app=leetcode.cn id=940 lang=python3
#
# [940] 不同的子序列 II
#

# @lc code=start
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mo = 1e9 + 7
        n = len(s)
        dp = [0] * (n + 5)
        dp[0] = 2
        dp[-1] = 1
        for i in range(1, n):
            flag = False
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i] = int((dp[i - 1] % mo * 2  - dp[j - 1] % mo) % mo)
                    flag = True
                    break
            if not flag:
                dp[i] = int((dp[i - 1] % mo * 2) % mo)
            dp[i] = int(dp[i] % mo)
        
        return int(((dp[n - 1] - 1) % mo))


# @lc code=end

