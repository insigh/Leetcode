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
You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
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
        self.get_level_nodes(root, 0)
        L = len(self.level_nodes)
        for i in range(L):
            count = len(self.level_nodes[i])
            for j in range(count):
                if j < count - 1:
                    self.level_nodes[i][j].next = self.level_nodes[i][j+1]
                else:
                    self.level_nodes[i][j].next = None
        
    def get_level_nodes(self, node, level):
        if not node:
            return 
        if node:
            if level in self.level_nodes:
                self.level_nodes[level].append(node)
            else:
                self.level_nodes[level] = [node]
        if node.left:
            print(node.left.val)
            self.get_level_nodes(node.left, level+1)
        if node.right:
            self.get_level_nodes(node.right, level+1)
            
            
        