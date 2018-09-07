"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        dummy_head = ListNode(0)
        progate = 0
        curr = dummy_head
        while l1 or l2 :
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0
            curr.next = ListNode((v1 + v2 + progate)%10)
            progate = (v1 + v2 + progate)//10
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next
        if progate != 0:
            curr.next = ListNode(progate)
        return dummy_head.next