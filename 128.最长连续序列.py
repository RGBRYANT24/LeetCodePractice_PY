#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_curve = 0

        for i in range(len(nums)):
            cur_num = nums[i]
            current_curve = 1
            if cur_num - 1 not in nums_set:

                while cur_num + 1 in nums_set:
                    cur_num += 1
                    current_curve += 1

                max_curve = max(max_curve, current_curve)
        return max_curve
# @lc code=end

