#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        flag = False
        if x < 0:
            flag = True
            x *= -1
        s = list(str(x))
        s.reverse()
        x = int(''.join(s))
        if flag:
            x *= -1
        return 0 if x > 2 ** 31 -1 or x < -1 * 2 ** 31 else x
# @lc code=end

