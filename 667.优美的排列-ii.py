#
# @lc app=leetcode.cn id=667 lang=python3
#
# [667] 优美的排列 II
#
# https://leetcode.cn/problems/beautiful-arrangement-ii/description/
#
# algorithms
# Medium (62.15%)
# Likes:    222
# Dislikes: 0
# Total Accepted:    31.3K
# Total Submissions: 47.2K
# Testcase Example:  '3\n1'
#
# 给你两个整数 n 和 k ，请你构造一个答案列表 answer ，该列表应当包含从 1 到 n 的 n 个不同正整数，并同时满足下述条件：
# 
# 
# 假设该列表是 answer = [a1, a2, a3, ... , an] ，那么列表 [|a1 - a2|, |a2 - a3|, |a3 -
# a4|, ... , |an-1 - an|] 中应该有且仅有 k 个不同整数。
# 
# 
# 返回列表 answer 。如果存在多种答案，只需返回其中 任意一种 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3, k = 1
# 输出：[1, 2, 3]
# 解释：[1, 2, 3] 包含 3 个范围在 1-3 的不同整数，并且 [1, 1] 中有且仅有 1 个不同整数：1
# 
# 
# 示例 2：
# 
# 
# 输入：n = 3, k = 2
# 输出：[1, 3, 2]
# 解释：[1, 3, 2] 包含 3 个范围在 1-3 的不同整数，并且 [2, 1] 中有且仅有 2 个不同整数：1 和 2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = [0] * n
        ans[0] = 1
        num_list = [i for i in range(2, n+1)]
        if k == 1:
            ans = [i for i in range(1, n+1)]
            return ans
        
        while k > 1:
            ans[n - k] = num_list[-1]
            num_list.pop() # 弹出最大的元素
            if k > 2:
                k -= 2
            else:
                break
        j = 0
        for i in range(n):
            if ans[i] == 0:
                ans[i] = num_list[j]
                j += 1
                
        return ans



# @lc code=end

