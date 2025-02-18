#User function Template for python3

class Solution:
    def changeBits(self, N):
        # code here 
        new_num = (1 << N.bit_length()) - 1 
        return [new_num - N, new_num] 
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        ans = ob.changeBits(N)
        
        print(ans[0],ans[1])
        print("~")
# } Driver Code Ends