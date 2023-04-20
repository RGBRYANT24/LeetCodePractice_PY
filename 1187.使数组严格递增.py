#
# @lc app=leetcode.cn id=1187 lang=python3
#
# [1187] 使数组严格递增
#
# https://leetcode.cn/problems/make-array-strictly-increasing/description/
#
# algorithms
# Hard (48.15%)
# Likes:    170
# Dislikes: 0
# Total Accepted:    11.1K
# Total Submissions: 18.9K
# Testcase Example:  '[1,5,3,6,7]\n[1,3,2,4]'
#
# 给你两个整数数组 arr1 和 arr2，返回使 arr1 严格递增所需要的最小「操作」数（可能为 0）。
# 
# 每一步「操作」中，你可以分别从 arr1 和 arr2 中各选出一个索引，分别为 i 和 j，0 <= i < arr1.length 和 0 <= j
# < arr2.length，然后进行赋值运算 arr1[i] = arr2[j]。
# 
# 如果无法让 arr1 严格递增，请返回 -1。
# 
# 
# 
# 示例 1：
# 
# 输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# 输出：1
# 解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。
# 
# 
# 示例 2：
# 
# 输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# 输出：2
# 解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。
# 
# 
# 示例 3：
# 
# 输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# 输出：-1
# 解释：无法使 arr1 严格递增。
# 
# 
# 
# 提示：
# 
# 
# 1 <= arr1.length, arr2.length <= 2000
# 0 <= arr1[i], arr2[i] <= 10^9
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        dp = [0] * len(arr1)
        n_2 = len(arr2)
        arr2.sort()
        num = arr1[0]
        for i in range(1, len(arr1)):
            if num < arr1[i]:
                dp[i] = dp[i - 1]
                continue
            else:
                index = bisect.bisect_left(arr2, num + 1)
                if index < n_2:
                    num = arr2[index] # 替换arr1中的数
                    dp[i] = dp[i - 1] + 1
                else: # 替换不了
                    return -1
        return dp[len(arr1) - 1]

# @lc code=end

