"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = []
        self.getMaxSum(root)
        self.dfs(root)
        return max(self.res)

    def dfs(self, node):
        if not node:
            return 0
        
        if node.left:
            self.dfs(node.left)
        if not node.left or not node.right:
            self.res.append(node.res)
        if node.left and node.right:
            self.res.append(max(node.res, node.res+min(node.left.res, node.right.res)))
        if node.right:
            self.dfs(node.right)
        
        
        
    def getMaxSum(self, node):
        
        if not node:
            return 0
        
        node.res = max(max(self.getMaxSum(node.left),self.getMaxSum(node.right)) + node.val,node.val)
        return node.res
        