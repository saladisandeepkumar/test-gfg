#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
def utility(n):
    # Return the winner as a string
    if n%2==1:
        return "You"
    else:
        return "Friend"


#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        
        ans = utility(n)
        print(ans)
        print('~')
# } Driver Code Ends