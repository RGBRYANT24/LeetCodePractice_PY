#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#
# https://leetcode.cn/problems/n-queens-ii/description/
#
# algorithms
# Hard (82.41%)
# Likes:    441
# Dislikes: 0
# Total Accepted:    120.7K
# Total Submissions: 146.5K
# Testcase Example:  '4'
#
# n 皇后问题 研究的是如何将 n 个皇后放置在 n × n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4
# 输出：2
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：1
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= n <= 9
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row):
            if row == n:
                return 1
            else:
                ans = 0
                for i in range(n):
                    if i + row in diag1 or row - i in diag2 or i in col:
                        continue
                    diag1.add(i + row)
                    diag2.add(row - i)
                    col.add(i)
                    queens[row] = i
                    ans += backtrack(row + 1)
                    diag1.remove(i + row)
                    diag2.remove(row - i)
                    col.remove(i)
                return ans

        diag1 = set()
        diag2 = set()
        col = set()
        queens = [-1] * n
        return backtrack(0)

# @lc code=end

