#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid
        return l
# @lc code=end

