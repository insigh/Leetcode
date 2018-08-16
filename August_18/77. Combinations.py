"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.list_ = [i+1 for i in range(n)]
        self.getAllcombines(n,k,0,-1,[])
        return self.res
    
    def getAllcombines(self,n,k,i,m,ans):
        if i==k:
            self.res.append(ans)
        else:
            for j in range(m+1,n-k+i+1):
                self.getAllcombines(n,k,i+1,j,ans+[self.list_[j]])
        
    
    