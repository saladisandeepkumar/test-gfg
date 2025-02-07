#User function Template for python3
import math

class Solution:
    def findPosition(self, n):
        # code here 
        return -1 if n==0 or (n&(n-1))!=0 else int(math.log(n,2)+1)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())

        ob = Solution()
        print(ob.findPosition(N))

# } Driver Code Ends