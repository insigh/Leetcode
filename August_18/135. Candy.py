"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:

Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
"""
class Solution:
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        
        L = len(ratings)
        
        res = 1
        inc, dec = 1, 1
        i = 1
        while i < L:
            # print(i)
            if ratings[i] > ratings[i-1]:
                if i > 1 and ratings[i-1] < ratings[i-2]:
                    inc = 1
                inc += 1
                res += inc
                dec = 1
                i += 1
                print(res)
            elif ratings[i] < ratings[i-1]:
                dec += 1
                res += dec -1
                if dec > inc:
                    res += 1
                i += 1
                print(res)
            else:
                res += 1
                inc, dec = 1, 1
                i += 1
                print(res)
        return res
            
        
                    
            
        
        