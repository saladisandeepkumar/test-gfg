
class Solution:
    def longestPalindrome(self, s):
        t = "#" + "#".join(s) + "#"
        n = len(t)
        p = [0] * n  
        center, right = 0, 0
        max_len, start = 0, 0
        for i in range(n):
            mirror = 2 * center - i 
            if i < right:
                p[i] = min(right - i, p[mirror]) 
            while i - p[i] - 1 >= 0 and i + p[i] + 1 < n and t[i - p[i] - 1] == t[i + p[i] + 1]:
                p[i] += 1
            if i + p[i] > right:
                center, right = i, i + p[i]
            if p[i] > max_len:
                max_len = p[i]
                start = (i - max_len) // 2 
        return s[start:start + max_len]



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends