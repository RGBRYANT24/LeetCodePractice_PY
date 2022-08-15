#
# @lc app=leetcode.cn id=792 lang=python3
#
# [792] 匹配子序列的单词数
#
# https://leetcode-cn.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (46.78%)
# Likes:    190
# Dislikes: 0
# Total Accepted:    10.6K
# Total Submissions: 22.7K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# 给定字符串 s 和字符串数组 words, 返回  words[i] 中是s的子序列的单词个数 。
# 
# 字符串的 子序列 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。
# 
# 
# 例如， “ace” 是 “abcde” 的子序列。
# 
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "abcde", words = ["a","bb","acd","ace"]
# 输出: 3
# 解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。
# 
# 
# Example 2:
# 
# 
# 输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# 输出: 2
# 
# 
# 
# 
# 提示:
# 
# 
# 1 <= s.length <= 5 * 10^4
# 1 <= words.length <= 5000
# 1 <= words[i].length <= 50
# words[i]和 s 都只由小写字母组成。
# 
# ​​​​
#

# @lc code=start
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        hash_table = {s : i for i, s in enumerate(words)}
        list.sort(words)
        pre = words[0]
        for i in range(len(words)):
            
# @lc code=end

