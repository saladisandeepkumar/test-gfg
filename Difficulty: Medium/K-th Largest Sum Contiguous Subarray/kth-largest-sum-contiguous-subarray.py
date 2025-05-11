from typing import List

import heapq
class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here
        pq=[]
        n=len(arr)
        for i in range(n):
            curr=0
            for j in range(i,n):
                curr+=arr[j]
                if len(pq)<k:
                    heapq.heappush(pq,curr)
                elif pq[0]<curr:
                    heapq.heapreplace(pq,curr)
        return heapq.heappop(pq)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

# Position this line where user code will be pasted.

#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.kthLargest(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends