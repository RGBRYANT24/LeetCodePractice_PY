#
# @lc app=leetcode.cn id=1144 lang=python3
#
# [1144] 递减元素使数组呈锯齿状
#
# https://leetcode.cn/problems/decrease-elements-to-make-array-zigzag/description/
#
# algorithms
# Medium (44.97%)
# Likes:    81
# Dislikes: 0
# Total Accepted:    18.3K
# Total Submissions: 37.8K
# Testcase Example:  '[1,2,3]'
#
# 给你一个整数数组 nums，每次 操作 会从中选择一个元素并 将该元素的值减少 1。
# 
# 如果符合下列情况之一，则数组 A 就是 锯齿数组：
# 
# 
# 每个偶数索引对应的元素都大于相邻的元素，即 A[0] > A[1] < A[2] > A[3] < A[4] > ...
# 或者，每个奇数索引对应的元素都大于相邻的元素，即 A[0] < A[1] > A[2] < A[3] > A[4] < ...
# 
# 
# 返回将数组 nums 转换为锯齿数组所需的最小操作次数。
# 
# 
# 
# 示例 1：
# 
# 输入：nums = [1,2,3]
# 输出：2
# 解释：我们可以把 2 递减到 0，或把 3 递减到 1。
# 
# 
# 示例 2：
# 
# 输入：nums = [9,6,1,6,2]
# 输出：4
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        def check(pos):
            res = 0
            for i in range(pos, len(nums), 2):
                a = 0
                if i - 1>= 0:
                    a = max(a, nums[i] - nums[i - 1] + 1)
                if i + 1 < len(nums):
                    a = max(a, nums[i] - nums[i + 1] + 1)
                res += a
            return res

        return min(check(0), check(1))
# @lc code=end

