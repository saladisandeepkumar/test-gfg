#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

#Write the complete function returnValueFunction below
#This function should take n as a parameter
#Return 2*n
#code here
def returnValueFunction(n):
    return 2*n


#{ 
 # Driver Code Starts.


def main():
    t=int(input())
    while(t>0):
        n=int(input())
        print(returnValueFunction(n))
        t-=1
        print("~")

if __name__ == "__main__": 
    main()
# } Driver Code Ends