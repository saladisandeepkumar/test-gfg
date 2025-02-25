#User function Template for python3
def nthDay(d, n):
    # code here
    return (d-n%7+7)%7


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        d, n = map(int, input().split())
        print(nthDay(d, n))
        print('~')

# } Driver Code Ends