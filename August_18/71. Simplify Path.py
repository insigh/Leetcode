"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

Corner Cases:

Did you consider the case where path = "/../"?
In this case, you should return "/".
Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
In this case, you should ignore redundant slashes and return "/home/foo".
"""
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        path = path.split('/')
        print(path)
        res ='/'
        stack = []
        for item in path:
            if item == '' or item == '.' or (item=='..' and not stack):
                continue
            elif item == '..':
                stack.pop(-1)
            else:
                stack.append(item)
        print(stack)
        return res+'/'.join(stack)
            
            