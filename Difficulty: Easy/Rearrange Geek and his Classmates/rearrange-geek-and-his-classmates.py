#User function Template for python3

class Solution:
    def prank(self, arr, n): 
        #code here
        for ind, num in enumerate(arr):
            num %=n
            arr[ind] += (arr[num] %n)*n
        for i in range(n):
            
            
            arr[i]//=n
            
            
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        ob = Solution()
        ob.prank(a, n)
        for i in a:
            print(i,end=" ")
        print()
        print("~")
# } Driver Code Ends