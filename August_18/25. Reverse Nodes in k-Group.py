"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head:
            return None
        count = 1
        temp = head
        while temp.next:
            count += 1
            temp = temp.next
            
         
        num_iters = count // k
        new_lists_head = head
        sofar_built_end = ListNode(-1)
        
        curr = head
        for i in range(num_iters):
            # print(i)
            Reversed_head = None
            Reversed_end = curr
            
            for j in range(k):
                next_ = curr.next
                curr.next = Reversed_head
                Reversed_head = curr
                curr = next_
                
            if i == 0:
                new_lists_head = Reversed_head
            sofar_built_end.next = Reversed_head
            sofar_built_end = Reversed_end
            
            if i == num_iters - 1:
                sofar_built_end.next = curr
        return new_lists_head
            