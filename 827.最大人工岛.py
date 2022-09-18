#
# @lc app=leetcode.cn id=827 lang=python3
#
# [827] 最大人工岛
#
# https://leetcode.cn/problems/making-a-large-island/description/
#
# algorithms
# Hard (39.69%)
# Likes:    259
# Dislikes: 0
# Total Accepted:    26.6K
# Total Submissions: 58.8K
# Testcase Example:  '[[1,0],[0,1]]'
#
# 给你一个大小为 n x n 二进制矩阵 grid 。最多 只能将一格 0 变成 1 。
# 
# 返回执行此操作后，grid 中最大的岛屿面积是多少？
# 
# 岛屿 由一组上、下、左、右四个方向相连的 1 形成。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: grid = [[1, 0], [0, 1]]
# 输出: 3
# 解释: 将一格0变成1，最终连通两个小岛得到面积为 3 的岛屿。
# 
# 
# 示例 2:
# 
# 
# 输入: grid = [[1, 1], [1, 0]]
# 输出: 4
# 解释: 将一格0变成1，岛屿的面积扩大为 4。
# 
# 示例 3:
# 
# 
# 输入: grid = [[1, 1], [1, 1]]
# 输出: 4
# 解释: 没有0可以让我们变成1，面积依然为 4。
# 
# 
# 
# 提示：
# 
# 
# n == grid.length
# n == grid[i].length
# 1 
# grid[i][j] 为 0 或 1
# 
# 
#

# @lc code=start



class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        tag = [[0] * n for _ in range(n)]
        area = Counter()
        def dfs(i, j):
            tag[i][j] = t 
            area[t] += 1
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if gird[x][y] != 0 and tag[x][y] == 0:
                    dfs(x, y)
# @lc code=end

