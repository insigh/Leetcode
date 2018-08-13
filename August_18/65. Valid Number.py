"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.
"""
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return re.match(r"^\s*[?:+-]?(([0-9]+\.?[0-9]*)|(\.[0-9]+))(?:(e[+-]?[0-9]+)?)\s*$",s.lower()) is not None

        