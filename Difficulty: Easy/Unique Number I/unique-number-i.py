class Solution:
    def findUnique(self, arr):
        # code here 
        unique_set = set()
        for num in arr:
            if num in unique_set:
                unique_set.remove(num)
            else:
                unique_set.add(num)
        return unique_set.pop()
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.findUnique(arr)
        print(ans)
        print("~")
# } Driver Code Ends