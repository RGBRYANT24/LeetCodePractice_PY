#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get(k):
            index1, index2 = 0, 0
            while True:
                if index1 == m:
                    # print('nums1 out', nums2[index2 + k - 1], index2, k)
                    return nums2[index2 + k - 1]
                if index2 == n:
                    return nums1[index1 + k - 1]
                if k == 1:
                    return min(nums1[index1], nums2[index2])

                new_index1 = min(index1 + k // 2 - 1, m - 1)
                new_index2 = min(index2 + k // 2 - 1, n - 1)
                pivot1 = nums1[new_index1]
                pivot2 = nums2[new_index2]
                # print(k, pivot1, pivot2, new_index1, new_index2, index1, index2)
                if pivot1 <= pivot2:
                    k -= new_index1 - index1 + 1
                    index1 = new_index1 + 1
                else:
                    k -= new_index2 - index2 + 1
                    index2 = new_index2 + 1
        m, n = len(nums1), len(nums2)
        total_length = m + n
        if (total_length) % 2 == 1:
            return get((total_length+ 1) // 2)
        else:
            # print('ans1')
            ans1 = get(total_length // 2 + 1)
            # print('ans2')
            ans2 = get(total_length // 2)
            return (ans1 + ans2) / 2
            
# @lc code=end

