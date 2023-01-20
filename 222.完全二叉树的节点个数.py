#
# @lc app=leetcode.cn id=222 lang=python3
#
# [222] 完全二叉树的节点个数
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        def get_h():
            node = root
            h = 0
            while node.left:
                node = node.left
                h += 1
            return h
        def exists(h, k) -> bool:
            
            bits = 1 << (h - 1)
            node = root
            while node != None and bits > 0:
                if not (bits & k): # 当前节点位置是0
                    node = node.left
                    # print('left', node.val)if node else print('left none')
                else:
                    
                    node = node.right
                    # print('right', node.val) if node else print('right none')
                bits >>= 1
            return not node == None # 判断这个节点存在不存在

        h = get_h()
        if h == 0:
            return 1
        # print('h', h)
        l, r = pow(2, h), pow(2, h + 1) - 1 # 由于完全二叉树最右下角的节点可能取到 所以要用左闭右闭区间
        while l <= r: # 左闭右闭区间要相错终止，即r < l
            mid = l + (r - l) // 2
            # mid = r - (r - l) // 2
            exist = exists(h, mid)
            # print(h, l, mid, r, exist)
            if exist:
                l = mid + 1 # 相错终止
            else:
                r = mid - 1 # 相错终止
        return r


        
# @lc code=end

