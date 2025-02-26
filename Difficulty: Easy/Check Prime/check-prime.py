#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

def prime(n):
    if n==1:
        return False
    for i in range(2,n,1):
        if n %i==0:
            return False
    return True
    
    # code here to check for prime.
    # return True or False


#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        ans = prime(n)
        print(ans)
        print("~")
# } Driver Code Ends