#
# @lc app=leetcode.cn id=307 lang=python3
#
# [307] 区域和检索 - 数组可修改
#
# https://leetcode-cn.com/problems/range-sum-query-mutable/description/
#
# algorithms
# Medium (52.49%)
# Likes:    405
# Dislikes: 0
# Total Accepted:    36K
# Total Submissions: 71.3K
# Testcase Example:  '["NumArray","sumRange","update","sumRange"]\n[[[1,3,5]],[0,2],[1,2],[0,2]]'
#
# 给你一个数组 nums ，请你完成两类查询。
# 
# 
# 其中一类查询要求 更新 数组 nums 下标对应的值
# 另一类查询要求返回数组 nums 中索引 left 和索引 right 之间（ 包含 ）的nums元素的 和 ，其中 left <= right
# 
# 
# 实现 NumArray 类：
# 
# 
# NumArray(int[] nums) 用整数数组 nums 初始化对象
# void update(int index, int val) 将 nums[index] 的值 更新 为 val
# int sumRange(int left, int right) 返回数组 nums 中索引 left 和索引 right 之间（ 包含
# ）的nums元素的 和 （即，nums[left] + nums[left + 1], ..., nums[right]）
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：
# ["NumArray", "sumRange", "update", "sumRange"]
# [[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
# 输出：
# [null, 9, null, 8]
# 
# 解释：
# NumArray numArray = new NumArray([1, 3, 5]);
# numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
# numArray.update(1, 2);   // nums = [1,2,5]
# numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= nums.length <= 3 * 10^4
# -100 <= nums[i] <= 100
# 0 <= index < nums.length
# -100 <= val <= 100
# 0 <= left <= right < nums.length
# 调用 update 和 sumRange 方法次数不大于 3 * 10^4 
# 
# 
#

# @lc code=start
class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.seg = [0]  * (self.n * 4)
        self.build(nums, 0, 0, self.n-1)
    
    def build(self, nums, node, l, r):
        if l == r :
            self.seg[node] = nums[l]
            return
        m = l + (r - l) // 2
        self.build(nums, node*2+1, l, m)
        self.build(nums, node*2+2, m+1, r)
        self.seg[node] = self.seg[node*2+1] + self.seg[node*2+2]

    def change(self, index, val, node, l, r):
        if l == r:
            self.seg[node] = val
            return
        m = l + (r - l) // 2
        if index <= m:
            self.change(index, val, node*2+1, l, m)
        else:
            self.change(index, val, node*2+2, m+1, r)
        self.seg[node] = self.seg[node*2+1] + self.seg[node*2+2]

    def range(self, sum_left, sum_right, node, l, r):
        if l == sum_left and r == sum_right:
            return self.seg[node]
        m = l + (r - l) // 2
        if sum_right <= m:
            return self.range(sum_left, sum_right, node*2+1, l, m)
        if sum_left > m:
            return self.range(sum_left, sum_right, node*2+2, m+1, r)
        return self.range(sum_left, m, node*2+1, l, m) + self.range(m+1, sum_right, node*2+2, m+1, r)

    def update(self, index: int, val: int) -> None:
        self.change(index, val, 0, 0, self.n-1)

    def sumRange(self, left: int, right: int) -> int:
        return self.range(left, right, 0, 0, self.n-1)



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
# @lc code=end

