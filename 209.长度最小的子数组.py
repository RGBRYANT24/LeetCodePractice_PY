#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s = [0]
        index = 0
        ans = len(nums)
        def check(i, j):
            if i == 0:
                return s[j]
            else:
                return s[j] - s[i - 1]
        
        if ans <= 1:
            return 1 if nums[-1] == target else 0
        for i in range(len(nums)):
            s.append(s[-1] + nums[i])
        for i in range(1, len(s)):
            tar = s[i - 1] + target
            bound = bisect.bisect_left(s, tar)
            # print(i, s[i], bound, tar)
            if bound != len(s):
                ans = min(ans, bound - i +1)
        # print(s)
        return 0 if s[-1] < target else ans

# @lc code=end

