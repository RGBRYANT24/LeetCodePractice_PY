#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        index = {s : i for i , s in enumerate(list1)}
        ans = []
        indexSum = inf
        for i, s in enumerate(list2):
            if i > indexSum:
                break
            if s in index:
                if i + index[s] < indexSum:
                    ans = []
                    ans.append(s)
                    indexSum = i + index[s]
                elif i + index[s] == indexSum:
                    ans.append(s)
        return ans


# @lc code=end

