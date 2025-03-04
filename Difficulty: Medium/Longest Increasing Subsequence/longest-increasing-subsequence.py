import bisect
class Solution:
    def lis(self, arr):
        # code here#
        sub = []   
        for x in arr:
            pos = bisect.bisect_left(sub, x)
            if pos == len(sub):
                sub.append(x)
            else:
                sub[pos] = x
        return len(sub)
       



#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends