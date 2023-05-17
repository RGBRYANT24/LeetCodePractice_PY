#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        inf = 1e9
        n = len(nums)
        dp = [inf] * (n + 5)
        dp[0] = 0
        for i in range(n):
            for j in range(i + 1, nums[i] + i + 1):
                if j < n:
                    dp[j] = min(dp[j], dp[i] + 1)
        return dp[n - 1]
# @lc code=end

