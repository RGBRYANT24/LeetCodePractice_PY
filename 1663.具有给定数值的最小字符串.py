#
# @lc app=leetcode.cn id=1663 lang=python3
#
# [1663] 具有给定数值的最小字符串
#

# @lc code=start
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        ans = [1] * n #全是a
        k = k - n
        for i in range(n - 1, -1, -1):
            if k >= 25:
                ans[i] = 26
                k -= 25
            else:
                ans[i] += k
                k = 0
        for i in range(n):
            ans[i] = chr(ans[i] + ord('a') - 1)
        return ''.join(ans)

# @lc code=end

