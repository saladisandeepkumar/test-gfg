import bisect

class Solution:
    def countLessEq(self, a, b):
        # code here
        b.sort()
        res =[]
        for ele in a :
            c = bisect.bisect_right(b,ele)
            res.append(c)
            
        return res
        
        