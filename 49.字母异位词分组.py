#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = collections.defaultdict(list)
        for s in strs:
            m = [0] *26
            for ch in s:
                m[ord(ch) - ord('a')] += 1
            d[tuple(m)].append(s)
        
        return list(d.values())
# @lc code=end

