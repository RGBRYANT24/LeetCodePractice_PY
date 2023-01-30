#
# @lc app=leetcode.cn id=287 lang=python3
#
# [287] 寻找重复数
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        l, r = 1, n + 1
        while l < r:
            mid = l + (r - l) // 2
            cnt = 0 
            for i in range(n + 1):
                if nums[i] <= mid:
                    cnt += 1
            if cnt <= mid:
                l = mid + 1
            else:
                r = mid
        return l
# @lc code=end

