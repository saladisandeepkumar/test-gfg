#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Your code her
        pq = []
        
        for x in points:
            a=x[0]
            b=x[1]
            
            dist = (a**2 + b**2)**0.5
            
            heapq.heappush(pq,(dist,(a,b)))
        
        ans = []
        
        while k>0:
            t = heapq.heappop(pq)
            
            a = t[1][0]
            b = t[1][1]
            
            ans.append((a,b))
            k-=1
            
        return ans
        

                
        
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends