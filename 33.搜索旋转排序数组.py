#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        nums.append(nums[-1])
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid
        min_index = r
        m = nums[-1]
        if min_index != 0:
            m = nums[r - 1]
        if target > nums[0] and target < m:
            l, r = 0, min_index
        elif target < nums[-1]:
            l, r = min_index, len(nums)
        else:
            return -1
        
        while l < r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            if target > mid:
                l = mid + 1
            else:
                r = mid
        if nums[l] == target:
            return l
        else:
            return -1

# @lc code=end

