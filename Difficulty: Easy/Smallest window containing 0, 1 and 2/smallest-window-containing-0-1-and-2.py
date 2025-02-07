#User function Template for python3

class Solution:
    def smallestSubstring(self, s):
        # Code here
        if len(s)<=2:
            return -1
        length=len(s)+1
        i=0
        j=2
        while j<len(s):
            while '0' in s[i:j+1]  and '1' in s[i:j+1]  and '2' in s[i:j+1] :
                length=min(length,j-i+1)
                i+=1
            j+=1
        return  length if length!=len(s)+1 else -1
                
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.smallestSubstring(S)

        print(ans)
        print("~")

# } Driver Code Ends