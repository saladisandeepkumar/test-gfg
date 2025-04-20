#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        ans=arr[0]
        for i in range(1,len(arr)):
            ans^=(arr[i]^i)
        return ans
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        print(ob.findDuplicate(arr))
        print("~")

# } Driver Code Ends