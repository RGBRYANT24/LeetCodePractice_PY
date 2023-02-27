#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def is_merge(s1, e1, s2, e2):
            if e1>= s2 or s1 >= s2:
                return min(s1, s2), max(e1, e2) 
            else:
                return -1, -1
        
        intervals.sort()
        start, end = intervals[0]
        index = 0
        while index < len(intervals) - 1:
            index_2 = index + 1
            start, end = is_merge(intervals[index][0], intervals[index][1], intervals[index_2][0], intervals[index_2][1])
            if start != -1:
                intervals[index] = [start, end]
                intervals.pop(index_2)
                continue
            print(index, intervals[index])
            index += 1
        
        return intervals
# @lc code=end

