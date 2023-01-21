#
# @lc app=leetcode.cn id=240 lang=python3
#
# [240] 搜索二维矩阵 II
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            ans = bisect.bisect_left(matrix[i], target)
            if ans < n and matrix[i][ans] == target:
                return True
        return False
# @lc code=end

