"""
Given a sorted linked list, delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.

"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        d = {}
        current = head
        while current is not None:
            if current.val not in d:
                d[current.val] = 1
            else:
                d[current.val] += 1
            current = current.next
        current = head
        dummy = ListNode(0)
        dummy_end = dummy
        while current is not None:
            if d[current.val] == 1:
                dummy_end.next = current
                dummy_end = current
            current = current.next
        dummy_end.next = None
        return dummy.next
