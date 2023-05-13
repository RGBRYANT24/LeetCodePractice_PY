#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_p = 1e9
        max_p = -1
        for p in prices:
            min_p = min(min_p, p)
            max_p = max(max_p, p - min_p)
        return max_p
# @lc code=end

