#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            dummyPoint = end.next
            end.next = None
            stk = []
            p = start
            while p:
                stk.append(p)
                p = p.next
            dummyHead = ListNode(-1)
            p = dummyHead
            # print('stk len', len(stk))
            while len(stk) > 0:
                p.next = stk.pop(-1)
                p = p.next
                # print(p.val)
            p.next = dummyPoint
            return dummyHead.next, dummyPoint, p
        
        d_head = ListNode(-1)
        d_head.next = head
        pre = d_head
        start = end = head
        while end:
            count = 1
            while count < k:
                count += 1
                if end.next:
                    end = end.next
                else:
                    return d_head.next
            pre.next, start, temp = reverse(start, end)
            pre = temp
            end = start
        return d_head.next
            
# @lc code=end

