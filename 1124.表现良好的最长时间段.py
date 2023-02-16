#
# @lc app=leetcode.cn id=1124 lang=python3
#
# [1124] 表现良好的最长时间段
#
# https://leetcode.cn/problems/longest-well-performing-interval/description/
#
# algorithms
# Medium (34.84%)
# Likes:    296
# Dislikes: 0
# Total Accepted:    24K
# Total Submissions: 67K
# Testcase Example:  '[9,9,6,0,6,6,9]'
#
# 给你一份工作时间表 hours，上面记录着某一位员工每天的工作小时数。
# 
# 我们认为当员工一天中的工作小时数大于 8 小时的时候，那么这一天就是「劳累的一天」。
# 
# 所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 大于「不劳累的天数」。
# 
# 请你返回「表现良好时间段」的最大长度。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：hours = [9,9,6,0,6,6,9]
# 输出：3
# 解释：最长的表现良好时间段是 [9,9,6]。
# 
# 示例 2：
# 
# 
# 输入：hours = [6,6,6]
# 输出：0
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= hours.length <= 10^4
# 0 <= hours[i] <= 16
# 
# 
#

# @lc code=start
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        s = [0]
        stk = [0]
        for i in range(len(hours)):
            score = -1
            if hours[i] > 8:
                score = 1
            s.append(s[-1] + score)
            if len(stk) < 1 or s[stk[-1]] > s[i]:
                # print(i, s[i], stk[-1], s[stk[-1]])
                stk.append(i)
        
        # return s, stk
        ans = 0
        for r in range(len(hours), 0, -1):
            while len(stk) > 0 and s[stk[-1]] < s[r]:
                l = stk[-1]
                # print(r, l)
                ans = max(ans, r - l)
                stk.pop(-1)
            
        return ans

# @lc code=end

