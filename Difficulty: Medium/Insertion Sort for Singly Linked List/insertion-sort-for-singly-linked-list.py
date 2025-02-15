#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    def insertionSort(self, head):
        #code here
        arr=[]
        while head:
            arr.append(head.data)
            head=head.next
        n = len(arr)
        for i in range(1, n):
            key = arr[i] 
            j = i-1
            while j >= 0 and arr[j] > key:
              arr[j + 1] = arr[j]
              j -= 1
            arr[j + 1] = key  
        for i in arr:
            print(i,end=" ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().insertionSort(head))

# } Driver Code Ends