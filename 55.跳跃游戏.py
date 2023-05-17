#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        end = nums[0]
        reach_max = 0
        n = len(nums) - 1
        while i <= end:
            end = max(i + nums[i], end)
            if n <= end:
                return True
            i += 1
        return False
# @lc code=end

