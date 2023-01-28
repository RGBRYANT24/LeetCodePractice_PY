#
# @lc app=leetcode.cn id=275 lang=python3
#
# [275] H 指数 II
#

# @lc code=start
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            target = n - mid
            if target == citations[mid]:
                return target
            if target > citations[mid]:
                l = mid + 1
            else:
                r = mid
        if l == 0:
            return n
        if l == n:
            return 0
        return min(citations[l], n - l)
# @lc code=end

