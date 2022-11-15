#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        
        dp = [[False] * n for _  in range(n)]
        for i in range(n):
            dp[i][i] = True
        
        maxi, maxj = 0, 0
        
        # traverse_list = []
        for L in range(2, n+1): # 枚举的是区间长度
            for i in range(n):
                j = L + i - 1 # j是右侧边界 因为L = j - i + 1推出
                if j >= n:
                    continue
                
                if s[i] != s[j]:
                    dp[i][j] = False
                
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]
                
                if dp[i][j]:
                    if L > maxj - maxi + 1:
                        maxi, maxj = i, j
                # traverse_list.append((i, j, dp[i][j]))
        # return traverse_list
        # return maxi, maxj
        return s[maxi : maxj + 1]
                    



# @lc code=end

