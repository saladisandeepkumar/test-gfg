#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def calculateSpan(self, arr):
        n=len(arr)
        ans=[0]*n
        s=[]
        for i in range(n):
            while s and s[-1][1]<=arr[i]:
                s.pop()
            ans[i]=i+1 if not s else i-s[-1][0]
            s.append((i,arr[i]))
        return ans
        #write code here

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends