from collections import deque

class Solution:
	def orangesRotting(self, mat):
		r,c=len(mat),len(mat[0])
		v=[[1 for i in range(c)] for j in range(r)]
		q=deque()
		ans=0
		for i in range(r):
		    for j in range(c):
		        if mat[i][j]==2:
		            q.append([i,j])
		            v[i][j]=0
		q.append(-1)
		while q:
		    ele=q.popleft()
		    if ele==-1:
		        if q:
		            q.append(-1)
		        else:
		            break
		        ans += 1
		        continue
		    m,n=ele[0],ele[1]
		    if (m+1)<r and v[m+1][n] and mat[m+1][n]==1:
		        v[m+1][n]=0
		        q.append([m+1,n])
		    if (m-1)>=0 and v[m-1][n] and mat[m-1][n]==1:
		        v[m-1][n]=0
		        q.append([m-1,n])
		    if (n+1)<c and v[m][n+1] and mat[m][n+1]==1:
		        v[m][n+1]=0
		        q.append([m,n+1])
		    if (n-1)>=0 and v[m][n-1] and mat[m][n-1]==1:
		        v[m][n-1]=0
		        q.append([m,n-1])
		for i in range(r):
		    for j in range(c):
		        if v[i][j]==mat[i][j]:
		            return -1
		return ans
#{ 
 # Driver Code Starts
from queue import Queue

T = int(input())
for i in range(T):
    n = int(input())
    m = int(input())
    mat = []
    for _ in range(n):
        a = list(map(int, input().split()))
        mat.append(a)
    obj = Solution()
    ans = obj.orangesRotting(mat)
    print(ans)
    print("~")

# } Driver Code Ends