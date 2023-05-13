#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, loc = m - 1, n - 1, m + n - 1
        while j >= 0:
            while i >= 0 and nums1[i] > nums2[j]:
                nums1[loc], nums1[i] = nums1[i], nums1[loc]
                i -= 1
                loc -= 1
            nums1[loc], nums2[j] = nums2[j], nums1[loc]
            loc -= 1
            j -= 1
        
# @lc code=end

