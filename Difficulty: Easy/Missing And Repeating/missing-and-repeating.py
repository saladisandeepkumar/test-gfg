#User function Template for python3
from collections import Counter
class Solution:
    def findTwoElement( self,arr): 
        # code here
        count = Counter(arr)
        return [max(arr, key=count.get), sum(range(1, len(arr) + 1)) - sum(set(arr))]
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends