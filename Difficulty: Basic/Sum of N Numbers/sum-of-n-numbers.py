#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

def nSum(n):
    
    ans = n*(n+1)//2
    
    #Write your code here to calculate and return sum of n number.
    
    
    return ans


#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        ans = nSum(n)
        print(ans)
        print("~")
# } Driver Code Ends