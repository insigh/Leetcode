"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root :
            return []
        self.sum = sum
        self.res = []
        self.findAllPath(root, root.val, [root.val])
        return self.res
    
        
    def findAllPath(self, root, sum_, path):
        if sum_ == self.sum and not root.left and not root.right:
            self.res.append(path)
        if not root:
            return 
        if root.left:
            self.findAllPath(root.left, sum_+root.left.val, path+[root.left.val])
        if root.right:
            self.findAllPath(root.right, sum_+root.right.val, path+[root.right.val])
        
        