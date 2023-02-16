#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'(' : ')', '[' : ']', '{' : '}'}
        stk = []
        for c in s:
            # print(stk)
            if c in d:
                stk.append(c)
                continue
            elif len(stk) > 0 and d[stk.pop()] == c:
                continue
            return False
            
        return True if len(stk) == 0 else False
# @lc code=end

