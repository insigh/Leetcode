"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.ip = [ str(i) for i in range(0,256)]
        self.res = []
        self.getAllips(s,[])
        return ['.'.join(ips) for ips in self.res]
    
    
    def getAllips(self,s,temp):
        if len(s)==0 and len(temp)==4:
            self.res.append(temp)
            return
        elif len(s)==0 or len(temp)==4:
            return 
        
        else:
            for i in range(min(len(s),1 if s[0]=='0' else 3)):
                if s[:i+1] in self.ip:
                    self.getAllips(s[i+1:],temp+[s[:i+1]])


                    