#
# @lc app=leetcode.cn id=1464 lang=python3
#
# [1464] 数组中两元素的最大乘积
#
# https://leetcode.cn/problems/maximum-product-of-two-elements-in-an-array/description/
#
# algorithms
# Easy (76.47%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    61.5K
# Total Submissions: 78.4K
# Testcase Example:  '[3,4,5,2]'
#
# 给你一个整数数组 nums，请你选择数组的两个不同下标 i 和 j，使 (nums[i]-1)*(nums[j]-1) 取得最大值。
# 
# 请你计算并返回该式的最大值。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [3,4,5,2]
# 输出：12 
# 解释：如果选择下标 i=1 和 j=2（下标从 0 开始），则可以获得最大值，(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1)
# = 3*4 = 12 。 
# 
# 
# 示例 2：
# 
# 输入：nums = [1,5,4,5]
# 输出：16
# 解释：选择下标 i=1 和 j=3（下标从 0 开始），则可以获得最大值 (5-1)*(5-1) = 16 。
# 
# 
# 示例 3：
# 
# 输入：nums = [3,7]
# 输出：12
# 
# 
# 
# 
# 提示：
# 
# 
# 2 <= nums.length <= 500
# 1 <= nums[i] <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = - 99
        b = - 100
        for num in nums:
            if a < num:
                b = a
                a = num
            elif b < num:
                b = num
        return (a - 1) * (b - 1)
# @lc code=end

