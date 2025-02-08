#User function Template for python3

class Solution():
    def solve(self, N, K, GeekNum):
        #your code goes here
        curr_sum = 0
        left = 0
        right = 0
        
        while right < N:
            curr_sum += GeekNum[right]
            if right - left + 1 > K:
                curr_sum -= GeekNum[left]
                left += 1
                
            if right == len(GeekNum) - 1:
                GeekNum.append(curr_sum)
            
            right += 1
        return GeekNum[len(GeekNum) - 2]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        N,K=map(int,input().split())
        GeekNum = [int(i) for i in input().split()]
        print(Solution().solve(N, K, GeekNum))
        
        print("~")
    
# } Driver Code Ends