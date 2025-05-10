#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
from collections import defaultdict
class Solution:
    def longestSubarray(self, arr, k):
        # Code Here
        sm = 0
        res = 0
        dc = defaultdict(int)
        dc[0] = -1
        for ind, num in enumerate(arr):
            sm += 1 if num >k else -1
            if sm > 0:
                res = max(res, ind+1)
            else:
                if sm not in dc:
                    dc[sm] = ind
                if sm-1 in dc:
                    res = max(res, ind - dc[sm-1])
            
        return res
                


#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        
        arr = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.longestSubarray(arr, k))
        print("~")
        t -= 1
# } Driver Code Ends