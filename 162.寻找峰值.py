#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        def get(index):
            if index < 0 or index >= n:
                return float('-inf')
            else:
                return nums[index]

        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if get(mid) > get(mid - 1) and get(mid) > get(mid + 1):
                return mid
            # print(mid, get(mid - 1), get(mid), get(mid + 1))
            if get(mid) < get(mid + 1):
                l = mid + 1
            else:
                r = mid
        
        return l
# @lc code=end

