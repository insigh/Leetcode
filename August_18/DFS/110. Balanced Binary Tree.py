"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:

Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def max_height(root):
            if not root:
                return 0
            return 1 + max(max_height(root.left), max_height(root.right))

        def check(node):
            if not node:
                return True
            if abs(max_height(node.left) - max_height(node.right)) > 1:
                return False
            return check(node.left) and check(node.right)

        return check(root)
