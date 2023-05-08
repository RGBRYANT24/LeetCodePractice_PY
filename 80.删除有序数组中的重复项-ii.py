#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除有序数组中的重复项 II
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        pre = nums[0]
        count = 1
        while i < len(nums):
            # print(nums, i, count, pre)
            if pre == nums[i]:
                count += 1
            else:
                count = 1
            if count > 2:
                nums.pop(i)
                count -= 1
            else:
                pre = nums[i]
                i += 1
            
        return len(nums)
# @lc code=end

