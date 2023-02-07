#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        if not head or not head.next:
            return None
        fast = head
        while fast != None:
            if not fast or not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            # print(slow.val, fast.val)
            if fast == slow:
                start = head
                while start != slow:
                    slow = slow.next
                    start = start.next
                return start
        return None
        
# @lc code=end

