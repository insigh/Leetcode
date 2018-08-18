"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:

Input:
    2
   / \
  1   3
Output: true
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfs(root,-2147483649,2147483648)
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
    def dfs(self,node,min_,max_):
        if not node:
            return True
        if node.val <= min_ or node.val >= max_:
            return False
        return self.dfs(node.left,min_,node.val) and self.dfs(node.right,node.val,max_)