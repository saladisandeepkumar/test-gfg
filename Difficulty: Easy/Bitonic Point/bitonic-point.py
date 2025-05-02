#User function Template for python3
class Solution:

	def findMaximum(self, arr):
		# code here
		l=0
        r=len(arr)
        while l<r:
            m=l+(r-l)//2
            if arr[m]>arr[m-1]:
                l=m+1
            else:
                r=m
        return arr[l-1]




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaximum(arr)
        print(ans)
        tc -= 1
        print("~")

# } Driver Code Ends