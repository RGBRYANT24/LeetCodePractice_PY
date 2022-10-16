#
# @lc app=leetcode.cn id=1790 lang=python3
#
# [1790] 仅执行一次字符串交换能否使两个字符串相等
#

# @lc code=start
from re import I


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        flag = False # 还没交换过
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                continue
            if s1[i] not in s2:
                return False
                # return 666
            if flag:
                return False
            for j in range(i+1, len(s1)):
                if s1[j] == s2[i] and s2[j] == s1[i]:
                    s1[i], s1[j] = s1[j], s1[i]
            flag = True

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        
        return True
# @lc code=end

