"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, curr_line, curr_len =[],[],0
        for word in words:
            if curr_len + len(word) + len(curr_line) > maxWidth:
                nSpace = maxWidth - curr_len
                for i in range(nSpace):
                    slots = len(curr_line)-1
                    if slots == 0:
                        curr_line[0] += ' '
                    else:
                        curr_line[i%slots] += ' '
                res.append(''.join(curr_line))
                curr_len = 0
                curr_line = []
            
            curr_len += len(word)
            curr_line.append(word)
        return res+[' '.join(curr_line).ljust(maxWidth)]
        
        