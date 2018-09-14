"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        if len(preorder) == 1:
            root = TreeNode(preorder[0])
            return root

        root = TreeNode(preorder[0])

        for i in range(len(inorder)):
            if inorder[i] == preorder[0]:
                break
        left_pre = preorder[1:1 + i]
        left_in = inorder[0:i]
        right_pre = preorder[1 + i:]
        right_in = inorder[1 + i:]
        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)
        return root
