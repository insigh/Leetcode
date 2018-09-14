"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

Example 1:

Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        def check(p, q):
            if p == None and q == None:
                return True
            if (q == None and p != None) or (q != None and p == None):
                return False
            if p.val != q.val:
                return False

            left = check(p.left, q.left)
            right = check(p.right, q.right)

            return left and right

        return check(p, q)


