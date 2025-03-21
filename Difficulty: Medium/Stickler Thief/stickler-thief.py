class Solution:  
    def findMaxSum(self,arr):
        # code here
        p1, p2 = 0, 0
        for num in arr:
            p1, p2 = p2, max(p2, p1 + num)
        return p2


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends