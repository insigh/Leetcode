"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        res = ListNode(-1)
        L = len(lists)
        pre_lists = lists
        while L>1:
            if L % 2 == 0:
                tmp_result = []
                for i in range(0,L,2):
                    tmp_result.append(self.merge2lists(pre_lists[i],pre_lists[i+1]))
            else:
                tmp_result = []
                for i in range(0,L-1,2):
                    tmp_result.append(self.merge2lists(pre_lists[i],pre_lists[i+1]))
                tmp_result.append(pre_lists[-1])
            pre_lists = tmp_result
            L = len(pre_lists)
        return pre_lists[0]
                    
        
    def merge2lists(self,L,R):
        res = ListNode(-1)
        temp = res
        while L or R:
            if L and R:
                if L.val > R.val:
                    temp.next = R
                    R = R.next
                    temp = temp.next
                else:
                    temp.next = L
                    L = L.next
                    temp = temp.next
            elif L:
                temp.next = L
                L = L.next
                temp = temp.next
            else:
                temp.next = R
                R = R.next
                temp = temp.next
                
        return res.next
            
            