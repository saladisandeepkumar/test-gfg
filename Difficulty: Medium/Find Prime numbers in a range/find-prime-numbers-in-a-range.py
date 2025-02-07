#User function Template for python3

class Solution:        
    def primeRange(self,M,N):
        #code here
        arr = [i if i>1 else 0 for i in range(N+1)]
        for i in range(2,N+1):
            for j in range(2*i,N+1,i):
                arr[j]=0
        return [i for i in range(M,N+1) if arr[i]]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        M,N=map(int,input().strip().split(" "))
        ob=Solution()
        ans=ob.primeRange(M,N)
        for i in ans:
            print(i,end=" ")
        print()    
        print("~")
# } Driver Code Ends