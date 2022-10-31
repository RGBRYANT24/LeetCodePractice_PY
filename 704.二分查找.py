#
# @lc app=leetcode.cn id=704 lang=python3
#
# [704] 二分查找
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while (l <= r):
            c = l + (r - l) // 2
            if nums[c] == target:
                return c
            if nums[c] < target:
                l = c + 1
            else:
                r = c - 1
        return -1
# @lc code=end

