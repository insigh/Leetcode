"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        res = self.getAllParenthesis(n,res,"",0,0)
        return res
    
        
    def getAllParenthesis(self,n,res,tmp,l,r):
        if l==r==n:
            res.append(tmp)
        else:
            if l>r:
                if l==n:
                    self.getAllParenthesis(n,res,tmp+")",l,r+1)
                else:
                    self.getAllParenthesis(n,res,tmp+"(",l+1,r)
                    self.getAllParenthesis(n,res,tmp+")",l,r+1)
            elif l==r:
                self.getAllParenthesis(n,res,tmp+"(",l+1,r)
                self.getAllParenthesis(n,res,tmp+")",l,r+1)
                
        return res
print(Solution().generateParenthesis(3))