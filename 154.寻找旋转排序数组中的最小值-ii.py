#
# @lc app=leetcode.cn id=154 lang=python3
#
# [154] 寻找旋转排序数组中的最小值 II
#

# @lc code=start
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(nums[n - 1])       
        # 还是左闭右开区间，但是为了和最右比较，要在nums[n]的位置上添加一个数
        # 因为有重复元素，所以这样不影响他的结果，也不影响单调性 
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                r -= 1
        return nums[r]

# @lc code=end

