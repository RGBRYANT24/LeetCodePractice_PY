#
# @lc app=leetcode.cn id=730 lang=python3
#
# [730] 统计不同回文子序列
#

# @lc code=start
class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
        mo = 1e9 + 7
        n = len(s)
        dp = [[0] * n for _ in range(n)] # 二维数组 记录i,j区间内的回文个数
        for i in range(n): #边界条件
            dp[i][i] = 1
        
        travers_list = []
        for L in range(2, n + 1): # 枚举区间 从小到大
            for i in range(n):
                j = L + i - 1 # L = j - i + 1
                if j >= n:
                    break
                if s[i] == s[j]:
                    low, high = i + 1, j - 1
                    for _ in range(L):
                        if low > high or s[low] == s[i] and s[high] == s[j]:
                            break
                        if s[low] != s[i]:
                            low += 1
                        if s[high] != s[j]:
                            high -= 1

                    if low > high:
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 2
                    if low == high:
                        dp[i][j] = 2 * dp[i + 1][j - 1] + 1
                    if low < high:
                        dp[i][j] = 2 * dp[i + 1][j - 1] - dp[low + 1][high - 1]
                
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]
                
                dp[i][j] = int(dp[i][j] % mo)
                travers_list.append((dp[i][j], s[i] == s[j], i, j, dp[i + 1][j - 1], dp[i][j - 1], dp[i + 1][j]))

                        



        # return travers_list
        return int(dp[0][n - 1] % mo)



# @lc code=end

