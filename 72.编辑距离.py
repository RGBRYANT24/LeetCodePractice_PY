#
# @lc app=leetcode.cn id=72 lang=python3
#
# [72] 编辑距离
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        la, lb = len(word1), len(word2)
        l = max(la, lb)
        dp = [[0] * (l + 5) for _ in range(l + 5)]
        for i in range(la + 1):
            dp[i][0] = i
        
        for i in range(lb + 1):
            dp[0][i] = i

        for i in range(1, la + 1):
            for j in range(1, lb + 1):
                left = dp[i - 1][j] + 1
                right = dp[i][j - 1] + 1
                mid = dp[i - 1][j - 1]
                if word1[i - 1] != word2[j - 1]:
                    mid += 1
                # dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] if word1[i - 1] == word2[j - 1] else dp[i - 1][j - 1] + 1)
                dp[i][j] = min(left, right, mid)
        return dp[la][lb]

# @lc code=end

