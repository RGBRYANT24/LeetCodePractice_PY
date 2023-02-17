#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        prev = prehead
        p1, p2 = list1, list2
        if prev == None:
            print('prev == None')
        while p1 and p2:
            if p1.val <= p2.val:
                prev.next = p1
                p1 = p1.next
            else:
                prev.next = p2
                p2 = p2.next
            if prev == None:
                print('prev == None', end = ' ')
            else:
                print('val', prev.val, end = ' ')
            prev = prev.next
            if prev == None:
                print('prev == None')
            else:
                print('val', prev.val)
        prev.next = p1 if p2 == None else p2
        return prehead.next

# @lc code=end

