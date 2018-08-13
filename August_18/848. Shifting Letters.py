"""
We have a string S of lowercase letters, and an integer array shifts.

Call the shift of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a'). 

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i+1 letters of S, x times.

Return the final string after all such shifts to S are applied.

Example 1:

Input: S = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: 
We start with "abc".
After shifting the first 1 letters of S by 3, we have "dbc".
After shifting the first 2 letters of S by 5, we have "igc".
After shifting the first 3 letters of S by 9, we have "rpl", the answer.
"""
class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        L = len(shifts)
        shifts = [item%26 for item in shifts]
        
        for j in range(L-1,-1,-1):
            if j != L-1:
                shifts[j] = shifts[j+1]+shifts[j]
            else:
                continue
        
        doc = 'abcdefghijklmnopqrstuvwxyz'
        ch2index = {ch:i for i,ch in enumerate(doc)}
        
        index2ch = {i:ch for (ch,i) in ch2index.items()}
        S = list(S)
        
        for i,ch in enumerate(S):
            S[i] = index2ch[(ch2index[ch]+shifts[i])%26]
        # print(shifts)   
        return ''.join(S)

        