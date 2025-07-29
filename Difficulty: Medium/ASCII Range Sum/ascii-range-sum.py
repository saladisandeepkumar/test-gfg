class Solution:
    def asciirange(self, s):
        # code here
        preSum=dict()
        currSum=0
        ans=dict()
        for item in s:
            currSum+=ord(item)
            if item in preSum:
                ans[item]=ans.get(item,0)+currSum-preSum[item]
            preSum[item]=currSum
        res=[]
        for key,value in ans.items():
            temp=value-ord(key)
            if temp:
                res.append(temp)
        return res