#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根 
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 1, x
        while l < r:
            mid = l + (r - l) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                r = mid 
            else:
                l = mid + 1
        return l - 1 if l * l > x else l

# @lc code=end

