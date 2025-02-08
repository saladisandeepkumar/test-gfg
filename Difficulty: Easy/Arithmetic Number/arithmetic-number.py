#User function Template for python3

class Solution:
    def inSequence(self, a, b, c):
        # code here
        for i in range(a,b+1,c):
            if i==b:
                return 1
        return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = int(input())
        B = int(input())
        C = int(input())
        ob = Solution()
        ans = ob.inSequence(A, B, C)
        if (ans):
            print("true")
        else:
            print("false")

# } Driver Code Ends