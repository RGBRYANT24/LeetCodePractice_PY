#
# @lc app=leetcode.cn id=74 lang=python3
#
# [74] 搜索二维矩阵
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        def get_xy(tot):
            # if tot <= 
            x = tot // n
            y = tot - n * x
            return x, y
        l, r = 0, len(matrix) * len(matrix[0])
        while l < r:
            mid = l + (r - l) // 2
            x, y = get_xy(mid)
            print(mid, x, y, matrix[x][y], m, n)
            if matrix[x][y] == target:
                return True
            if matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid
        x, y = get_xy(l)
        print(l, x, y, m, n)
        return True if x <= m - 1 and y <= n - 1 and matrix[x][y] == target else False
            
# @lc code=end

