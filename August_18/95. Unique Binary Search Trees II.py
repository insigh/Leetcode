"""
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   """
   # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
        
import copy

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        
        if not n:
            return []
        
        self.temp = {}
        
        return self.dfs(1,n)
        
    def dfs(self,from_,to_):
        if from_ > to_:
            return [None]
        if from_ == to_:
            node = TreeNode(from_)
            trees = [node]
            return trees
        
        if (from_,to_) in self.temp.keys():
            return self.temp[(from_,to_)]
        
        trees = []
        for i in range(from_,to_+1):
            left_trees = self.dfs(from_,i-1)
            right_trees = self.dfs(i+1,to_)
            node = TreeNode(i)
            for left_node in left_trees:
                for right_node in right_trees:
                    # node = TreeNode(i)
                    node.left = left_node
                    node.right = right_node
                    trees.append(copy.deepcopy(node))
        self.temp[(from_,to_)] = trees
        return trees
            
            
           
