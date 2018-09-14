"""
Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.nodes = []
        self.first_node = None
        self.second_node = None
        self.prev_node = TreeNode(-2347483648)
        self.in_order_travelsal(root)
        # print([node.val for node in self.nodes])
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val

    def in_order_travelsal(self, root):

        if not root:
            return

        if root.left:
            self.in_order_travelsal(root.left)

        if (not self.first_node and self.prev_node.val >= root.val):
            self.first_node = self.prev_node
        if (self.first_node and self.prev_node.val >= root.val):
            self.second_node = root

        self.prev_node = root

        if root.right:
            self.in_order_travelsal(root.right)
