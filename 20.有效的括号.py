#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        d = {'}':'{', ']':'[', ')':'(' , '?':'?'}
        # print(d.keys(), '(' in d)
        stk = ['?']
        for c in s:
            if not c in d:
                stk.append(c)
            elif stk.pop() != d[c]:
                return False
        return len(stk) == 1
# @lc code=end

