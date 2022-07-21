#
# @lc app=leetcode.cn id=814 lang=python3
#
# [814] 二叉树剪枝
#
# https://leetcode.cn/problems/binary-tree-pruning/description/
#
# algorithms
# Medium (70.21%)
# Likes:    288
# Dislikes: 0
# Total Accepted:    47.9K
# Total Submissions: 66.4K
# Testcase Example:  '[1,null,0,0,1]'
#
# 给你二叉树的根结点 root ，此外树的每个结点的值要么是 0 ，要么是 1 。
# 
# 返回移除了所有不包含 1 的子树的原二叉树。
# 
# 节点 node 的子树为 node 本身加上所有 node 的后代。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：root = [1,null,0,0,1]
# 输出：[1,null,0,null,1]
# 解释：
# 只有红色节点满足条件“所有不包含 1 的子树”。 右图为返回的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：root = [1,0,1,0,0,0,1]
# 输出：[1,null,1,null,1]
# 
# 
# 示例 3：
# 
# 
# 输入：root = [1,1,0,1,1,0,1,0]
# 输出：[1,1,0,1,1,null,1]
# 
# 
# 
# 
# 提示：
# 
# 
# 树中节点的数目在范围 [1, 200] 内
# Node.val 为 0 或 1
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root != None and root.left != None:
            root.left = self.pruneTree(root.left) # DFS
            """if root != None and root.left.val == 0: # DFS结束后他的左孩子应该是一棵符合标注的树
                root.left == None"""

        if root != None and root.right != None:
            root.right = self.pruneTree(root.right) # DFS
            """if root != None and root.right.val == 0: # DFS结束后他的右孩子应该是一棵符合标注的树
                root.right == None"""
             
        if root.val == 0 and root.left == None and root.right == None:
            root = None
        return root


# @lc code=end

