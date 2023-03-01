#
# @lc app=leetcode.cn id=2373 lang=python3
#
# [2373] 矩阵中的局部最大值
#

# @lc code=start
class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        def max_pool(x, y):#以x, y为左上角起点的3x3矩阵
            ans = 0
            for i in range(3):
                ans = max(ans, max(grid[x + i][y : y+ 3]))
            return ans
        n = len(grid)
        res = []
        for i in range(n-2):
            temp = []
            for j in range(n-2):
                temp.append(max_pool(i, j))
            res.append(temp)
        return res
# @lc code=end

