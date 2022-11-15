#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        count = 2
        ans = 0
        first, second = 2, 1
        if n <= 2:
            return 1 if n == 1 else 2 
        while count < n:
            ans = first + second
            first, second = ans, first
            count += 1
        return ans


# @lc code=end

