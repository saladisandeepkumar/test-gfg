def utility(number):
    # Code here
    return {1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}.get(number,"Unknown")



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        number = int(input())
        print(utility(number))
        t -= 1

# } Driver Code Ends