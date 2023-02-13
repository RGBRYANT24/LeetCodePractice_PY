#
# @lc app=leetcode.cn id=713 lang=python3
#
# [713] 乘积小于 K 的子数组
#
# https://leetcode.cn/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (49.23%)
# Likes:    645
# Dislikes: 0
# Total Accepted:    93.5K
# Total Submissions: 189.8K
# Testcase Example:  '[10,5,2,6]\n100'
#
# 给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
# 
# 
# 示例 1：
# 
# 
# 输入：nums = [10,5,2,6], k = 100
# 输出：8
# 解释：8 个乘积小于 100 的子数组分别为：[10]、[5]、[2],、[6]、[10,5]、[5,2]、[2,6]、[5,2,6]。
# 需要注意的是 [10,5,2] 并不是乘积小于 100 的子数组。
# 
# 
# 示例 2：
# 
# 
# 输入：nums = [1,2,3], k = 0
# 输出：0
# 
# 
# 
# 提示: 
# 
# 
# 1 <= nums.length <= 3 * 10^4
# 1 <= nums[i] <= 1000
# 0 <= k <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        product = 1
        ans = 0 
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right: # 滑动窗口内是不符合要求的子串 所以才要滑动
                # print(nums[left:right+1])
                product /= nums[left]
                left += 1
            ans += right - left + 1 # 注意记录连续子数组个数的方法 实际上就是 l - r + 1
        return ans

# @lc code=end

