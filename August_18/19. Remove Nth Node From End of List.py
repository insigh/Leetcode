"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 1
        temp = head
        while temp.next:
            temp = temp.next
            count += 1
        
        new_head = ListNode(-1)
        pre = new_head
        pre.next =head
        tmp = head
        i = 1
        while i<count-n+1:
            pre = tmp
            tmp=tmp.next
            i+=1
        pre.next = tmp.next
        return new_head.next
head=ListNode(1)
temp = head
for i in range(2,6):
	new_node = ListNode(i)
	temp.next=new_node
	temp = new_node

new_head = Solution().removeNthFromEnd(head,2)
while new_head:
	print(new_head.val)
	new_head=new_head.next

