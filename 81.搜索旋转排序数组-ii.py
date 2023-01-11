#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums)
        nums.append(nums[-1])
        while l < r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return True
            if nums[mid] == nums[l] and nums[mid] == nums[r]: # 两遍都是重复元素 有重复元素就退一格
                l += 1
                r -= 1
            elif nums[mid] >= nums[l]: #左侧有序
                if target >= nums[l] and target < nums[mid]: # 左侧有序就首先要考虑向左侧转移的情况
                    r = mid
                else:
                    # 不满足左侧有序 或者 target在左侧找不到就要向右转移
                    l = mid + 1
            else: # 右侧有序
                if target <= nums[r] and target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid
        return True if target == nums[l] else False
# @lc code=end

