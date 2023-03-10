#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除有序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        p1, p2 = 0, 1
        while p2 < len(nums):
            while p2 < len(nums) and nums[p1] == nums[p2]:
                nums.pop(p2)
            p1 = p2
            p2 += 1
            if p2 >= len(nums):
                break
        return len(nums)
# @lc code=end

