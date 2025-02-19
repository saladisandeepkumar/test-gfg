#User function Template for python3

class Solution:
    def count(self, n: int) -> int:
        #your code here
        dp = [1] + [0] * n
        for score in [3, 5, 10]:
            for i in range(score, n + 1):
                dp[i] += dp[i - score]
        return dp[n]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        ob = Solution()
        print(ob.count(n))
        
        print("~")
# } Driver Code Ends