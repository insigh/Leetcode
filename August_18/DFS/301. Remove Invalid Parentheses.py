"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""


class Solution:
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        left = s.count('(')
        right = s.count(')')
        min_ = min(left, right)
        res = []

        def dfs(s, l, r, temp):

            if not s and l == r:
                res.append(temp)
                return

            if l < r or not s:
                return

            if s[0] == '(':
                if l < min_:
                    dfs(s[1:], l + 1, r, temp + s[0])
                dfs(s[1:], l, r, temp)

            if s[0] == ')':
                if r < min_:
                    dfs(s[1:], l, r + 1, temp + s[0])
                dfs(s[1:], l, r, temp)

            if s[0] not in '()':
                dfs(s[1:], l, r, temp + s[0])

        dfs(s, 0, 0, '')
        res_ = {}
        if res:
            max_len = len(max(res, key=lambda x: len(x)))

            for item in res:
                if len(item) == max_len:
                    res_[item] = None

        return list(res_.keys()) if res_ else [""]

