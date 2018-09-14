"""
Given a binary tree

struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:

You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.
"""


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.level_nodes = {}

        def get_level_nodes(node, level):
            if not node:
                return
            if level in self.level_nodes:
                self.level_nodes[level].append(node)
            else:
                self.level_nodes[level] = [node]
            if node.left:
                get_level_nodes(node.left, level + 1)
            if node.right:
                get_level_nodes(node.right, level + 1)

        get_level_nodes(root, 0)
        for level in self.level_nodes.keys():
            nodes = self.level_nodes[level]
            count = len(nodes)
            for i in range(count - 1):
                nodes[i].next = nodes[i + 1]
            nodes[count - 1].next = None
