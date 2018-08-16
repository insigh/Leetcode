class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        L,l = len(s),len(t)
        if L<l:
            return ""
        inversed_index = {}
        for i in range(L):
            if s[i] not in inversed_index.keys():
                inversed_index[s[i]]= [i]
            else:
                inversed_index[s[i]].append(i)
        # print(inversed_index)
        t = list(t)
        # print(t)
        bak = []
        for item in t:
            if item in inversed_index.keys():
                bak.append(inversed_index[item])
            else:
                return ""
        # print(bak)

        i,j = self.find_shortest(bak)
        # print(i,j)
        if i is None and j is None:
            return ""
        # print(self.find_shortest(bak))
        return s[i:j+1]
        
        
        
    def find_shortest(self,nums):
        # import copy
        # M = len(array)
        # N = [ len(array[i]) for i in range(M)]
        # min_gap = 2147483647
        # res = [[i] for i in array[0]]
        # i = 1
        # print(M)
        # while i < M:
        #     # temp = []
        #     temp = res
        #     res = []
        #     for j in range(len(array[i])):
        #         for item in temp:
        #             res.append(item+[array[i][j]])
        #     i += 1
        #     print(i)
        # print(res)
        
        # res = self.remove_duplicate(res)
        # if not res:
        #     return None,None
        
        # start,end = 0,min_gap
        # for list_ in res:
        #     if max(list_)-min(list_) < min_gap:
        #         min_gap = max(list_)-min(list_)
        #         start = min(list_)
        #         end = max(list_)
                
        # return start,end
        L = R = None
        while True:
            mn = mx = nums[0][-1]
            ind = [0]
            for i, ls in enumerate(nums[1:]):
                if ls[-1] > mx:
                    mx, ind = ls[-1], [i + 1]
                elif ls[-1] == mx:
                    ind.append(i + 1)
                elif ls[-1] < mn:
                    mn = ls[-1]
            if L == None or mx - mn <= R - L:
                L, R = mn, mx
            for j in ind:
                nums[j].pop()
                if not nums[j]:
                    return [L, R]
    def remove_duplicate(self,res):
        ans = []
        for item in res:
            dict_ = {i:"" for i in item}
            if len(dict_.keys()) == len(item):
                ans.append(item)
        print(ans)
        return ans
        
        
print(Solution().minWindow("ask_not_what_your_country_can_do_for_you_ask_what_you_can_do_for_your_country","ask_country"))