#
# @lc app=leetcode.cn id=122 lang=python3
#
# [122] 买卖股票的最佳时机 II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = min_p = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[i - 1]: # 不是当前递增单调区间
                ans += max_p - min_p
                # print(max_p, min_p, i, ans)
                max_p = min_p = prices[i]

            else:
                max_p = prices[i]
        if prices[-1] > min_p:
            ans += prices[-1] - min_p
        return ans
# @lc code=end

