

'''
给定两个字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true 
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/check-permutation-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        def default_index():
            return -1
        
        cnt1, cnt2 = [0] * 200, [0] *200
        for i in range(len(s1)):
            index = ord(s1[i])
            cnt1[index] += 1 
        for i in range(len(s2)):
            index = ord(s2[i])
            cnt2[index] += 1
        
        for i in range(len(cnt1)):
            if cnt1[i] != cnt2[i]:
                return False
        
        return True