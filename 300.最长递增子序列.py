#
# @lc app=leetcode.cn id=300 lang=python3
#
# [300] 最长递增子序列
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * (n + 5)
        dp[0] = 1
        travers_list = []
        for i in range(1, n):
            for j in range(i):
                if dp[i] <= dp[j] and nums[i] > nums[j]:
                    dp[i] = dp[j] + 1
                    travers_list.append((i, j, dp[i], dp[i], nums[i], nums[j]))
        
        return max(dp)
                
# @lc code=end

