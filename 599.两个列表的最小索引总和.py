#
# @lc app=leetcode.cn id=599 lang=python3
#
# [599] 两个列表的最小索引总和
#

# @lc code=start
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        ans = []
        count_min = 9999
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    if count_min > i + j:
                        ans = []
                        ans.append(list1[i])
                        count_min = i + j
                    elif count_min == i + j:
                        ans.append(list1[i])
        return ans

# @lc code=end

