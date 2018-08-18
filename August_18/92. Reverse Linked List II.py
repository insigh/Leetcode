"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        
        temp = head
        dummy_head = None
        
        k = 1
        pre = None
            
        while temp:
            if k < m:
                pre = temp
                temp = temp.next
                k += 1
            elif k < n:
                if k == m :
                    dummy_tail = temp
                next_ = temp.next
                temp.next = dummy_head
                dummy_head = temp
                temp = next_
                k += 1
            elif k == n:
                next_ = temp.next
                temp.next = dummy_head
                dummy_head = temp
                if pre:
                    pre.next = dummy_head
                dummy_tail.next = next_
                break
        if pre:
            return head
        else:
            return dummy_head
                
                
                
                
        