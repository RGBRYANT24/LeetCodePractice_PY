#
# @lc app=leetcode.cn id=167 lang=python3
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def bin_search(x):
            l, r = 0, len(numbers)
            while l < r:
                mid = l + (r - l) // 2
                # print(x, l, mid, r)
                if numbers[mid] == x:
                    # print('return', mid, numbers[mid], x)
                    return mid
                if numbers[mid] < x:
                    l = mid + 1
                else:
                    r = mid
            # print(x, l, r)
            return l if l < len(numbers) and numbers[l] == x else -1
        for i in range(len(numbers)):
            ans = []
            temp = bin_search(target - numbers[i])
            if temp == i:
                continue
            # print(i, numbers[i], temp)
            if temp != -1:
                ans.append(i + 1)
                ans.append(temp + 1)
                ans.sort()
                return ans
            # if numbers[i] <= target:
                
        
        return ans.sort()
# @lc code=end

