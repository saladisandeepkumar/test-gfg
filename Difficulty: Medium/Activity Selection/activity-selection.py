class Solution:
    def activitySelection(self, start, finish):
        #code here
        n=len(start)
        activities=sorted(zip(start,finish), key=lambda x:x[1])
        activity_count=1
        last_finish_time=activities[0][1]
        for i in range(1,n):
            if activities[i][0]>last_finish_time:
                activity_count+=1
                last_finish_time=activities[i][1]
        return activity_count


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Number of test cases

    for _ in range(t):
        # Read the start times
        start = list(map(int, input().strip().split()))

        # Read the finish times
        finish = list(map(int, input().strip().split()))

        # Create solution object and call activitySelection
        obj = Solution()
        print(obj.activitySelection(start, finish))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends