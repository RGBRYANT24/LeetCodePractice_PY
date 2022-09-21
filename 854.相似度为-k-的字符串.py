#
# @lc app=leetcode.cn id=854 lang=python3
#
# [854] 相似度为 K 的字符串
#
# https://leetcode.cn/problems/k-similar-strings/description/
#
# algorithms
# Hard (37.16%)
# Likes:    163
# Dislikes: 0
# Total Accepted:    8.3K
# Total Submissions: 20.1K
# Testcase Example:  '"ab"\n"ba"'
#
# 对于某些非负整数 k ，如果交换 s1 中两个字母的位置恰好 k 次，能够使结果字符串等于 s2 ，则认为字符串 s1 和 s2 的 相似度为 k 。
# 
# 给你两个字母异位词 s1 和 s2 ，返回 s1 和 s2 的相似度 k 的最小值。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s1 = "ab", s2 = "ba"
# 输出：1
# 
# 
# 示例 2：
# 
# 
# 输入：s1 = "abc", s2 = "bca"
# 输出：2
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= s1.length <= 20
# s2.length == s1.length
# s1 和 s2  只包含集合 {'a', 'b', 'c', 'd', 'e', 'f'} 中的小写字母
# s2 是 s1 的一个字母异位词
# 
# 
#

# @lc code=start
import queue


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        step, n = 0, len(s1)
        q, vis = [(s1, 0)], {s1}
        step = 0
        while True:
            tmp = q
            q = []
            for s, i in tmp:
                if s == s2:
                    return step
                while i < n and s[i] == s2[i]:
                    i += 1
                for j in range(i+1, n):
                    if s[j] == s2[i] != s2[j]: # 只有在匹配上正确的字符串 并且交换有意义的时候交换 （剪枝了）
                        temp_s = list(s)
                        temp_s[i], temp_s[j] = temp_s[j], temp_s[i]
                        temp_s = ''.join(temp_s)
                        if temp_s not in vis:
                            q.append((temp_s, i+1))
                            vis.add(temp_s)
            step += 1
'''
针对每一层的bfs 可以把每一层单独存放一个队列
'''           
        

'''
"abccaacceecdeea"
"bcaacceeccdeaae"
'''

# @lc code=end

