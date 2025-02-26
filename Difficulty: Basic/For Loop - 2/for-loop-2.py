#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3


def utility(s):
    print("".join(s[::2]),end="")
    # Your code here


#{ 
 # Driver Code Starts.



def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        s=input().strip()
        utility(s)
        print()##separating testcases outputs by newlines
        testcases-=1
        


        print("~")
if __name__=='__main__':
    main()
# } Driver Code Ends