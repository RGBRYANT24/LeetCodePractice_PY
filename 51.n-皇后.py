#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#
# https://leetcode.cn/problems/n-queens/description/
#
# algorithms
# Hard (74.13%)
# Likes:    1783
# Dislikes: 0
# Total Accepted:    309.5K
# Total Submissions: 417.3K
# Testcase Example:  '4'
#
# 按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
# 
# n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
# 
# 给你一个整数 n ，返回所有不同的 n 皇后问题 的解决方案。
# 
# 
# 
# 每一种解法包含一个不同的 n 皇后问题 的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 4
# 输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# 解释：如上图所示，4 皇后问题存在两个不同的解法。
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：[["Q"]]
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
    def solveNQueens(self, n: int) -> List[List[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                r[queens[i]] = 'Q'
                board.append(''.join(r))
                r[queens[i]] = '.'
            return board
                

        def backtrack(row):
            if row == n:
                temp = generateBoard()
                ans.append(temp)

            else:
                for i in range(n):
                    if i + row in diag1 or row - i in diag2 or i in col:
                        continue
                    diag1.add(i + row)
                    diag2.add(row - i)
                    col.add(i)
                    queens[row] = i
                    backtrack(row + 1)
                    queens[row] = -1
                    diag1.remove(i + row)
                    diag2.remove(row - i)
                    col.remove(i)




        ans = list()
        diag1 = set()
        diag2 = set()
        col =  set()
        queens = [-1] * n
        r = ['.'] * n
        backtrack(0)
        return ans
# @lc code=end

