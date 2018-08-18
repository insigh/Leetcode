"""
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.dfs(1,n,[0]*n)
        
    def dfs(self,from_,to_,cache):
        if from_ >= to_ :
            return 1
        if cache[to_ - from_]:
            return cache[to_ - from_]
        total = 0
        for i in range(from_,to_+1):
            total += self.dfs(from_,i-1,cache)*self.dfs(i+1,to_,cache)
        cache[to_ - from_] = total
        return total
            
        
        
        
        