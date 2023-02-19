#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        prehead = ListNode(-1)
        pre = prehead
        while True:
            index = 0
            # print('len lists', len(lists))
            if len(lists) == 0:
                return prehead.next
            while len(lists) > 0 and not lists[index]:
                
                index += 1
                # print('index', index)
                if index >= len(lists):
                    return prehead.next
                # print(index, len(lists), lists[index] == None)
                
            # print(index, lists[index].val)
            for i in range(len(lists)):
                if lists[i] and lists[index] and lists[i].val < lists[index].val:
                    index = i
            pre.next = lists[index]
            lists[index] = lists[index].next
            pre = pre.next
            # print(pre.val)
            # print(len(lists), 'len')
            flag = False
            # print(index)
# @lc code=end

