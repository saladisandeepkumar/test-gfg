class Solution:
    def equalPartition(self, arr):
        # code here
        total_sum = sum(arr)
        if total_sum % 2 != 0:
            return False
        target = total_sum // 2
        bitmask = 1  
        for num in arr:
            bitmask |= bitmask << num  
        return (bitmask & (1 << target)) != 0
        


#{ 
 # Driver Code Starts
import sys

input = sys.stdin.readline

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        if ob.equalPartition(arr):
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends