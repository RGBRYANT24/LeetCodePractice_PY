#
# @lc app=leetcode.cn id=2341 lang=python3
#
# [2341] 数组能形成多少数对
#

# @lc code=start
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        d = list(d.values())
        ans1 = 0
        ans2 = 0
        for x in d:
            ans1 += x // 2
            ans2 += x % 2
        return [ans1, ans2]

# @lc code=end

