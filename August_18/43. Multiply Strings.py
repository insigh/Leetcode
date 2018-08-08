"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1_list = [int(num) for num in num1]
        num2_list = [int(num) for num in num2]
        res = self.getListProduct(num1_list,num2_list)
        res = self.getSum(res)
        if self.checkAllZero(res):
            return "0"
        else:
            return res
    def checkAllZero(self,res):
        flag = True
        for item in res:
            if item != "0":
                return False
        return True

    def getListProduct(self,list1,list2):
        
        res = []
        
        for i,num2 in enumerate(list(reversed(list2))):
            res.append(self.getnumProduct(list1,num2)+'0'*i)
        return res
            
        
    def getnumProduct(self,list1,num):
        res = []
        add = 0
        for i,num1 in enumerate(list(reversed(list1))):
            temp = (num)*num1
            res.append((temp+add)%10)
            add = (temp+add)//10
        if add > 0:
            res.append(add)
        return "".join([str(num) for num in list(reversed(res))])
    
    
    def getSum(self,list_):
        res = []
        cnt_num = len(list_)
        max_len = len(max(list_,key=len))
        list_ = [ "0"*(max_len-len(num))+num  for num in list_]
        list_ = [ list(reversed([int(item) for item in num])) for num in list_]
        add = 0
        for i in range(max_len):
            temp = 0
            for j in range(len(list_)):
                temp += list_[j][i]
            res.append((temp+add)%10)
            add = (temp+add)//10
        if add > 0:
            res.append(add)
        
        return "".join([str(num) for num in list(reversed(res))])
            
                
        
            
            
            
            
print(Solution().multiply("123","456"))