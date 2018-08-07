"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        key_values = {"2":['a','b','c'],"3":['d','e','f'],"4":['g','h','i'],"5":['j','k','l'],"6":['m','n','o'],"7":['p','q','r','s'],"8":['t','u','v'],"9":['w','x','y','z']}
        
        if not digits:
            return []
        res = []
        res = self.getAllcombinations(key_values,digits,res,"",0)
        return res
        
        
    def getAllcombinations(self,key_values,digits,res,tmp,index):
        if index == len(digits):
            res.append(tmp)
        else:
            digit = digits[index]
            for ch in key_values[digit]:
                self.getAllcombinations(key_values,digits,res,tmp+ch,index+1)
        return res
        
print(Solution().letterCombinations("23"))