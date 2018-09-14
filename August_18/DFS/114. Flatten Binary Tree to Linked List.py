"""
Given a binary tree, flatten it to a linked list in-place.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        def preorder(node, node_list):
            if not node:
                return node_list
            node_list.append(node)
            preorder(node.left, node_list)
            preorder(node.right, node_list)
            return node_list

        node_list = preorder(root, [])
        if not node_list:
            return
        for i, node in enumerate(node_list):
            node.left = None
            if i != len(node_list) - 1:
                node.right = node_list[i + 1]
            else:
                node.right = None

