"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example:

Input: [1,2,3]
    1
   / \
  2   3
Output: 25
Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.res = []
        self.dfs(root, '')
        self.res = list(map(int, self.res))
        return sum(self.res)

    def dfs(self, node, temp):
        if not node.left and not node.right:
            self.res.append(temp + str(node.val))
            # return
        else:
            if node.left:
                self.dfs(node.left, temp + str(node.val))
            if node.right:
                self.dfs(node.right, temp + str(node.val))
