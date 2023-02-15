#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = list()
        n = len(nums)
        # print(nums)
        def check(i, j, k):
            if nums[i] + nums[j] + nums[k] == 0:
                ans.append([nums[i], nums[j], nums[k]])
        
        for first in range(n):
            # 需要枚举的数和上一次的不同
            if first > 0 and nums[first] == nums[first - 1] :
                continue
            third = n - 1 # 注意双指针更新的位置 肯定不能是third嵌套在second的for循环里面
            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue
                
                while third > second and nums[first] + nums[second] + nums[third] >= 0:
                    if third == second:
                        break
                    if third < n - 1 and nums[third] == nums[third + 1]:
                        third -= 1
                        continue
                    check(first, second, third)
                    # print(first, second, third, nums[first], nums[second], nums[third])
                    third -= 1
        return ans
            

# @lc code=end

